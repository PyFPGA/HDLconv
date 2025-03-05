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

Alternatives
------------
