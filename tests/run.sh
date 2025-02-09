#!/bin/bash

set -e

export PYTHONPATH=$(pwd)/..

#
# Sanity
#

python3 ../hdlconv/vhdl2vhdl.py --top Counter hdl/vhdl/counter.vhdl

python3 ../hdlconv/vhdl2vlog.py --top Counter hdl/vhdl/counter.vhdl

python3 ../hdlconv/slog2vlog.py --top Counter hdl/slog/counter.sv

#
# vhdl2vhdl
#

python3 ../hdlconv/vhdl2vhdl.py --filename conv1.vhdl \
  --top Counter hdl/vhdl/counter.vhdl

python3 ../hdlconv/vhdl2vhdl.py --filename conv2.vhdl \
  --generic FREQ 10000000 --generic SECS 1 --arch Arch --top Top \
  hdl/vhdl/blink.vhdl,blink_lib hdl/vhdl/blink_pkg.vhdl,blink_lib hdl/vhdl/top.vhdl

#
# vhdl2vlog
#

python3 ../hdlconv/vhdl2vlog.py --filename conv3.v --top Counter hdl/vhdl/counter.vhdl

python3 ../hdlconv/vhdl2vlog.py --filename conv4.v \
  --generic FREQ 10000000 --generic SECS 1 --arch Arch --top Top \
  hdl/vhdl/blink.vhdl,blink_lib hdl/vhdl/blink_pkg.vhdl,blink_lib hdl/vhdl/top.vhdl

python3 ../hdlconv/vhdl2vlog.py --backend yosys --filename conv5.v \
  --top Counter hdl/vhdl/counter.vhdl

python3 ../hdlconv/vhdl2vlog.py --backend yosys --filename conv6.v \
  --generic FREQ 10000000 --generic SECS 1 --arch Arch --top Top \
  hdl/vhdl/blink.vhdl,blink_lib hdl/vhdl/blink_pkg.vhdl,blink_lib hdl/vhdl/top.vhdl

#
# slog2vlog
#

python3 ../hdlconv/slog2vlog.py --filename conv7.v \
  --top Counter hdl/slog/counter.sv

python3 ../hdlconv/slog2vlog.py --filename conv8.v \
  --include hdl/slog/include1 --include hdl/slog/include2 \
  --define DEFINE1 1 --define DEFINE2 1 \
  --param FREQ 10000000 --param SECS 1 \
  --top Top hdl/slog/blink.sv hdl/slog/top.sv

python3 ../hdlconv/slog2vlog.py --frontend synlig --filename conv9.v \
  --top Counter hdl/slog/counter.sv

python3 ../hdlconv/slog2vlog.py --frontend synlig --filename convA.v \
  --include hdl/slog/include1 --include hdl/slog/include2 \
  --define DEFINE1 1 --define DEFINE2 1 \
  --param FREQ 10000000 --param SECS 1 \
  --top Top hdl/slog/blink.sv hdl/slog/top.sv

python3 ../hdlconv/slog2vlog.py --frontend yosys --filename convB.v \
  --top Counter hdl/slog/counter.sv

python3 ../hdlconv/slog2vlog.py --frontend yosys --filename convC.v \
  --include hdl/slog/include1 --include hdl/slog/include2 \
  --define DEFINE1 1 --define DEFINE2 1 \
  --param FREQ 10000000 --param SECS 1 \
  --top Top hdl/slog/blink.sv hdl/slog/top.sv

#
# Misc
#

# More than one Docker volume

cp hdl/vhdl/top.vhdl /tmp

python3 ../hdlconv/vhdl2vhdl.py --filename convD.vhdl \
  --generic FREQ 10000000 --generic SECS 1 --arch Arch --top Top \
  hdl/vhdl/blink.vhdl,blink_lib hdl/vhdl/blink_pkg.vhdl,blink_lib /tmp/top.vhdl
