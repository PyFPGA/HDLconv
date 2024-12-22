# HDLconv

HDL converter (between VHDL, SystemVerilog and/or Verilog), based on [GHDL](https://github.com/ghdl/ghdl), [Yosys](https://github.com/YosysHQ/yosys), [Synlig](https://github.com/chipsalliance/synlig) and the plugins [ghdl-yosys-plugin](https://github.com/ghdl/ghdl-yosys-plugin) and [yosys-slang](https://github.com/povik/yosys-slang).
It relies on [Docker](https://docs.docker.com/get-docker) and [PyFPGA containers](https://github.com/PyFPGA/containers).

* `vhdl2vhdl`: converts from a newer VHDL to VHDL'93 (using `ghdl`).
* `vhdl2vlog`: converts from VHDL to Verilog (backends: `ghdl` or `yosys`).
* `slog2vlog`: converts from SystemVerilog to Verilog (frontends: `slang`, `synlig` or `yosys`).

# Documentation

```
usage: vhdl2vhdl [-h] [-v] [-g GENERIC VALUE] [-a ARCH] [-f FILENAME]
                 [-o PATH] [-t TOPNAME]
                 FILE[,LIBRARY] [FILE[,LIBRARY] ...]

VHDL to VHDL

positional arguments:
  FILE[,LIBRARY]        VHDL file/s (with an optional LIBRARY specification)

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -g GENERIC VALUE, --generic GENERIC VALUE
                        specify a top-level Generic (can be specified multiple
                        times)
  -a ARCH, --arch ARCH  specify a top-level Architecture
  -f FILENAME, --filename FILENAME
                        resulting file name [<TOPNAME>.vhdl]
  -o PATH, --odir PATH  output directory [results]
  -t TOPNAME, --top TOPNAME
                        specify the top-level of the design
```

```
usage: vhdl2vlog [-h] [-v] [--backend TOOL] [-g GENERIC VALUE] [-a ARCH]
                 [-f FILENAME] [-o PATH] [-t TOPNAME]
                 FILE[,LIBRARY] [FILE[,LIBRARY] ...]

VHDL to Verilog

positional arguments:
  FILE[,LIBRARY]        VHDL file/s (with an optional LIBRARY specification)

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --backend TOOL        backend tool [ghdl]
  -g GENERIC VALUE, --generic GENERIC VALUE
                        specify a top-level Generic (can be specified multiple
                        times)
  -a ARCH, --arch ARCH  specify a top-level Architecture
  -f FILENAME, --filename FILENAME
                        resulting file name [<TOPNAME>.v]
  -o PATH, --odir PATH  output directory [results]
  -t TOPNAME, --top TOPNAME
                        specify the top-level of the design
```

```
usage: slog2vlog [-h] [-v] [--frontend TOOL] [-p PARAM VALUE]
                 [-d DEFINE VALUE] [-i PATH] [-f FILENAME] [-o PATH]
                 [-t TOPNAME]
                 FILE [FILE ...]

SystemVerilog to Verilog

positional arguments:
  FILE                  System Verilog file/s

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --frontend TOOL       frontend tool [slang]
  -p PARAM VALUE, --param PARAM VALUE
                        specify a top-level Parameter (can be specified
                        multiple times)
  -d DEFINE VALUE, --define DEFINE VALUE
                        specify a Define (can be specified multiple times)
  -i PATH, --include PATH
                        specify an Include Path (can be specified multiple
                        times)
  -f FILENAME, --filename FILENAME
                        resulting file name [<TOPNAME>.v]
  -o PATH, --odir PATH  output directory [results]
  -t TOPNAME, --top TOPNAME
                        specify the top-level of the design
```
