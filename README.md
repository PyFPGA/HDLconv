# HDLconv

HDL converter (between VHDL, SystemVerilog and/or Verilog), based on [GHDL](https://github.com/ghdl/ghdl), [Yosys](https://github.com/YosysHQ/yosys), [Synlig](https://github.com/chipsalliance/synlig) and the plugins [ghdl-yosys-plugin](https://github.com/ghdl/ghdl-yosys-plugin) and [yosys-slang](https://github.com/povik/yosys-slang).
It relies on [Docker](https://docs.docker.com/get-docker) and [PyFPGA containers](https://github.com/PyFPGA/containers).

* `vhdl2vhdl`: converts from a newer VHDL to VHDL'93 (using `ghdl`).
* `vhdl2vlog`: converts from VHDL to Verilog (backends: `ghdl` or `yosys`).
* `slog2vlog`: converts from SystemVerilog to Verilog (frontends: `slang`, `synlig` or `yosys`).
