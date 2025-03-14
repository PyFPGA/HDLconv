Introduction
============

HDL converter provides a set of command-line utilities for converting between VHDL, SystemVerilog, and Verilog.
Those, gathers files and options, then orchestrates the execution of the following tools - either separately or in combination when required.

* `GHDL <https://github.com/ghdl/ghdl>`_
* `Yosys <https://github.com/YosysHQ/yosys>`_
* `Synlig <https://github.com/chipsalliance/synlig>`_
* `ghdl-yosys-plugin <https://github.com/ghdl/ghdl-yosys-plugin>`_
* `yosys-slang <https://github.com/povik/yosys-slang>`_

To avoid the need to install multiple tools, it relies on `Docker <https://docs.docker.com/get-docker>`_ and `PyFPGA containers <https://github.com/PyFPGA/containers>`_.

Command-line utilities
----------------------

* ``vhdl2vhdl``: converts from a newer VHDL to VHDL'93.
    * Solved using ``ghdl``.
* ``vhdl2vlog``: converts from VHDL to Verilog. This has two alternatives:
    * Purely ``ghdl`` (**default**).
    * Uses ``ghdl-yosys-plugin`` as frontend and ``yosys`` as backend.
* ``slog2vlog``: converts from SystemVerilog to Verilog. This has three alternatives:
    * Uses ``yosys-slang`` as frontend and ``yosys`` as backend (**default**).
    * Purely ``synlig`` (based on ``Surelog`` and ``yosys``).
    * Purely ``yosys`` (simpler SV support, but could be sufficient in some cases).

.. note::
   Multiple alternatives are provided so you can try different options if one does not work.
