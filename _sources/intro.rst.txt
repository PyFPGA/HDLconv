Introduction
============

HDL converter (between VHDL, SystemVerilog and/or Verilog), based on `GHDL <https://github.com/ghdl/ghdl>`_, `Yosys <https://github.com/YosysHQ/yosys>`_, `Synlig <https://github.com/chipsalliance/synlig>`_ and the plugins `ghdl-yosys-plugin <https://github.com/ghdl/ghdl-yosys-plugin>`_ and `yosys-slang <https://github.com/povik/yosys-slang>`_.

It relies on `Docker <https://docs.docker.com/get-docker>`_ and `PyFPGA containers <https://github.com/PyFPGA/containers>`_.

* ``vhdl2vhdl``: converts from a newer VHDL to VHDL'93 (using ``ghdl``).
* ``vhdl2vlog``: converts from VHDL to Verilog (backends: ``ghdl`` or ``yosys``).
* ``slog2vlog``: converts from SystemVerilog to Verilog (frontends: ``slang``, ``synlig`` or ``yosys``).
