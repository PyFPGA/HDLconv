from setuptools import setup, find_packages

import hdlconv

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='HDLconv',
    version= hdlconv.__version__,
    description='HDL converter, based on GHDL, Yosys, and the plugins ghdl-yosys-plugin and yosys-slang',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rodrigo A. Melo',
    author_email='rodrigomelo9@gmail.com',
    license='GPLv3',
    url='https://github.com/PyFPGA/HDLconv',
    package_data={'': ['templates/*.jinja']},
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'vhdl2vhdl = hdlconv.vhdl2vhdl:main',
            'vhdl2vlog = hdlconv.vhdl2vlog:main',
            'slog2vlog = hdlconv.slog2vlog:main'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Utilities',
        'Topic :: Software Development :: Build Tools',
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)"
    ],
    install_requires=['jinja2']
)
