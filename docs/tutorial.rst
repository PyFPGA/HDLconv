Tutorial
========

Installation
------------

HDLconv can be installed from PyPi with:

.. code-block:: bash

   pip install hdlconv

Docker should be installed and able to run as a normal user.
Instructions for Linux `here <https://docs.docker.com/desktop/setup/install/linux>`_.

.. note::

   HDLconv relies on containers that are based on Linux systems.

.. hint::

   Do you prefer to use tools installed on your system instead? Use the ``--no-docker`` option.

Basic
-----

Mandatory arguments are the name of the top-level module/entity and at least one HDL file:

.. code-block:: bash

   vhdl2vhdl --top Counter counter.vhdl
   vhdl2vlog --top Counter counter.vhdl
   slog2vlog --top Counter counter.sv

Any of these commands create the ``results`` directory, containing three files:

* ``counter.log``: contains ``STDOUT`` and ``STDERR`` messages from the underlying tool, mainly useful for debugging errors.
* ``counter.sh``: the bash script executed under the hood.
* ``counter.v[hdl]``: the resulting converted HDL file.

.. note::

   The basename of the resulting file is, by default, the top-level name in lowercase.

.. hint::

   Are HDLconv options not enough for you? You can always manually customize and run the resulting bash script ;-)

The output directory and basename for the resulting files can be specified as follows:

.. code-block:: bash

   vhdl2vhdl --top Counter --odir newdir --filename newfile.vhdl counter.vhdl

Advanced
--------

When the input files are VHDL, libraries can be specified by adding a semicolon after the file path:

.. code-block:: bash

   vhdl2vhdl -top Top blink.vhdl,blink_lib blink_pkg.vhdl,blink_lib top.vhdl

While generics values and the desired architecture are specified as follows:

.. code-block:: bash

   vhdl2vlog --generic FREQ 10000000 --generic SECS 1 --arch Arch --top Counter counter.vhdl

For SystemVerilog inputs, you can specify parameters values, defines, and directories to be included:

.. code-block:: bash

   slog2vlog --param FREQ 10000000 --param SECS 1 --define DEFINE1 1 --define DEFINE2 1 \
       --include hdl/slog/include1 --include hdl/slog/include2 --top Counter counter.sv

Alternatives
------------

The ``vhdl2vhdl`` script is solved using only ``ghdl``, but others provide more than one alternative, where frontend or backend tools are modified.

By default, ``vhdl2vlog`` uses only ``ghdl``, but the combination of ``ghdl-yosys-plugin`` and ``yosys`` can be used instead, specifying the desired backend:

.. code-block:: bash

   vhdl2vlog --backend yosys --top Counter counter.vhdl

By default, ``slog2vlog`` uses the combination of ``yosys-slang`` and ``yosys``, referred to as ``slang`` for simplicity, but an alternative frontend can be specified.
One alternative is to use ``synlig``, a synthesizer based on ``surelog`` and ``yosys``, as follows:

.. code-block:: bash

   slog2vlog --frontend synlig --top Counter counter.sv

The other option is to simply use ``yosys``, which has simpler SystemVerilog support but could be sufficient in some cases:

.. code-block:: bash

   slog2vlog --frontend yosys --top Counter counter.sv
