# HDLconv

HDL converter (between VHDL, SystemVerilog and/or Verilog), based on [GHDL](https://github.com/ghdl/ghdl), [Yosys](https://github.com/YosysHQ/yosys), [Synlig](https://github.com/chipsalliance/synlig) and the plugins [ghdl-yosys-plugin](https://github.com/ghdl/ghdl-yosys-plugin) and [yosys-slang](https://github.com/povik/yosys-slang).
It relies on [Docker](https://docs.docker.com/get-docker) and [PyFPGA containers](https://github.com/PyFPGA/containers).

* `vhdl2vhdl`: converts from a newer VHDL to VHDL'93 (using `ghdl`).
* `vhdl2vlog`: converts from VHDL to Verilog (backends: `ghdl` or `yosys`).
* `slog2vlog`: converts from SystemVerilog to Verilog (frontends: `slang`, `synlig` or `yosys`).

# Documentation

```
usage: vhdl2vhdl [-h] [-v] [--generic GENERIC VALUE] [--arch ARCH]
                 [-t TOPNAME] [--filename FILENAME]
                 FILE[,LIBRARY] [FILE[,LIBRARY] ...]

VHDL to VHDL

positional arguments:
  FILE[,LIBRARY]        VHDL file/s (with an optional LIBRARY specification)

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --generic GENERIC VALUE
                        specify a top-level Generic (can be specified multiple
                        times)
  --arch ARCH           specify a top-level Architecture
  -t TOPNAME, --top TOPNAME
                        specify the top-level of the design
  --filename FILENAME   resulting file name [<TOPNAME>.vhdl]
```

```
usage: vhdl2vlog [-h] [-v] [--backend TOOL] [--generic GENERIC VALUE]
                 [--arch ARCH] [-t TOPNAME] [--filename FILENAME]
                 FILE[,LIBRARY] [FILE[,LIBRARY] ...]

VHDL to Verilog

positional arguments:
  FILE[,LIBRARY]        VHDL file/s (with an optional LIBRARY specification)

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --backend TOOL        backend tool [ghdl]
  --generic GENERIC VALUE
                        specify a top-level Generic (can be specified multiple
                        times)
  --arch ARCH           specify a top-level Architecture
  -t TOPNAME, --top TOPNAME
                        specify the top-level of the design
  --filename FILENAME   resulting file name [<TOPNAME>.v]
```

```
usage: slog2vlog [-h] [-v] [--frontend TOOL] [--param PARAM VALUE]
                 [--define DEFINE VALUE] [--include PATH] [-t TOPNAME]
                 [--filename FILENAME]
                 FILE [FILE ...]

SystemVerilog to Verilog

positional arguments:
  FILE                  System Verilog file/s

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --frontend TOOL       backend tool [slang]
  --param PARAM VALUE   specify a top-level Parameter (can be specified
                        multiple times)
  --define DEFINE VALUE
                        specify a Define (can be specified multiple times)
  --include PATH        specify an Include Path (can be specified multiple
                        times)
  -t TOPNAME, --top TOPNAME
                        specify the top-level of the design
  --filename FILENAME   resulting file name [<TOPNAME>.v]
```
