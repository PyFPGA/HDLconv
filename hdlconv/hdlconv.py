#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 HDLconv Project
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

"""HDLconv: HDL converter"""

import argparse
import glob
import os
import shutil
import subprocess
import sys


from jinja2 import Environment, FileSystemLoader
from os import chdir
from pathlib import Path
from __init__ import __version__ as version


LANGS = {
    'vhdl': 'VHDL',
    'vlog': 'Verilog',
    'slog': 'SystemVerilog'
}


def check_docker():
    if shutil.which('docker') is None:
        print(
            'ERROR: Docker is not installed. Instructions at: '
            'https://docs.docker.com/engine/install'
        )
        sys.exit(1)

def get_args(src, dst):
    """Get arguments from the CLI"""
    MULTIMSG = '(can be specified multiple times)'
    prog = f'{src}2{dst}'
    description = f'{LANGS[src]} to {LANGS[dst]}'
    parser = argparse.ArgumentParser(prog=prog, description=description)
    if src == 'vhdl':
        metavar = 'FILE[,LIBRARY]'
        help = 'VHDL file/s (with an optional LIBRARY specification)'
    else:
        metavar = 'FILE'
        help = 'System Verilog file/s'
    filename = '<TOPNAME>.vhdl' if dst == 'vhdl' else '<TOPNAME>.v'
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'HDLconv - v{version}'
    )
    if src == 'slog':
        parser.add_argument(
            '--frontend',
            metavar='TOOL',
            default='slang',
            choices=['slang', 'synlig', 'yosys'],
            help='backend tool [slang]'
        )
    if src == 'vhdl' and dst == 'vlog':
        parser.add_argument(
            '--backend',
            metavar='TOOL',
            default='ghdl',
            choices=['ghdl', 'yosys'],
            help='backend tool [ghdl]'
        )
    if src == 'vhdl':
        parser.add_argument(
            '--generic',
            metavar=('GENERIC', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a top-level Generic {MULTIMSG}'
        )
        parser.add_argument(
            '--arch',
            metavar='ARCH',
            help='specify a top-level Architecture'
        )
    else:
        parser.add_argument(
            '--param',
            metavar=('PARAM', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a top-level Parameter {MULTIMSG}'
        )
        parser.add_argument(
            '--define',
            metavar=('DEFINE', 'VALUE'),
            action='append',
            nargs=2,
            help=f'specify a Define {MULTIMSG}'
        )
        parser.add_argument(
            '--include',
            metavar='PATH',
            action='append',
            help=f'specify an Include Path {MULTIMSG}'
        )
    parser.add_argument(
        '-t', '--top',
        metavar='TOPNAME',
        help='specify the top-level of the design'
    )
    parser.add_argument(
        '--filename',
        metavar='FILENAME',
        default=filename,
        help=f'resulting file name [{filename}]'
    )
    parser.add_argument(
        'files',
        metavar=metavar,
        nargs='+',
        help=help
    )
    return parser.parse_args()

def get_data(src, dst, args):
    """Get data from arguments.

    :raises NotADirectoryError: when a directory is not found
    :raises FileNotFoundError: when a file is not found
    """
    data = {}
    data['hdl'] = 'raw-vhdl' if dst == 'vhdl' else 'verilog'
    data['top'] = args.top
    data['filename'] = args.filename
    if 'arch' in args and args.arch:
        data['arch'] = args.arch
    if 'generic' in args and args.generic:
        for generic in args.generic:
            data.setdefault('generics', {})[generic[0]] = generic[1]
    if 'param' in args and args.param:
        for param in args.param:
            data.setdefault('params', {})[param[0]] = param[1]
    if 'define' in args and args.define:
        for define in args.define:
            data.setdefault('defines', {})[define[0]] = define[1]
    if 'include' in args and args.include:
        for include in args.include:
            include = Path(include).resolve()
            if not include.is_dir():
                raise NotADirectoryError(include)
            data.setdefault('includes', []).append(include)
    for file in args.files:
        if src == 'vhdl':
            aux = file.split(',')
            file = Path(aux[0]).resolve()
            if not file.exists():
                raise FileNotFoundError(file)
            lib = aux[1] if len(aux) > 1 else None
            data.setdefault('files', {})[file] = lib
        else:
            file = Path(file).resolve()
            if not file.exists():
                raise FileNotFoundError(file)
            data.setdefault('files', []).append(file)
    return data

def get_template(src, dst, args):
    template = 'ghdl'
    if src == 'slog':
        if args.frontend == 'slang':
            template = 'slang-yosys'
        else:
            template = args.frontend
    if src == 'vhdl' and dst == 'vlog':
        if args.backend == 'yosys':
            template = 'ghdl-yosys'
    return template

def get_content(tempname, tempdata):
    """Get script to run."""
    tempdir = Path(__file__).parent.joinpath('templates')
    jinja_file_loader = FileSystemLoader(str(tempdir))
    jinja_env = Environment(loader=jinja_file_loader)
    jinja_template = jinja_env.get_template(f'{tempname}.jinja')
    return jinja_template.render(tempdata)

def run_tool(content, filename):
    old_dir = Path.cwd()
    new_dir = Path('temp')
    new_dir.mkdir(parents=True, exist_ok=True)
    chdir(new_dir)
    script = Path(filename).with_suffix(".sh")
    with open(script, 'w', encoding='utf-8') as fhandler:
        fhandler.write(content)
    command = f'bash {script}'
    try:
        log = Path(filename).with_suffix(".log")
        with open(log, 'w', encoding='utf-8') as fhandler:
            subprocess.run(
                command, shell=True, check=True, text=True,
                stdout=fhandler, stderr=fhandler
            )
        print(f'INFO: {filename} created')
    except subprocess.CalledProcessError:
        print(f'ERROR: check {log} for details')
        sys.exit(1)
    finally:
        for cf in glob.glob("*.cf"):
            os.remove(cf)
        shutil.rmtree("slpp_all", ignore_errors=True)
        os.chdir(old_dir)

def HDLconv(src, dst):
    check_docker()
    args = get_args(src, dst)
    data = get_data(src, dst, args)
    template = get_template(src, dst, args)
    content = get_content(template, data)
    run_tool(content, args.filename)
