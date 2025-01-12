#!/bin/bash

export PYTHONPATH=$(pwd)

file="README.md"
pattern="# Documentation"

lines=()

while IFS= read -r line; do
    if [[ "$line" =~ $pattern ]]; then
        break
    fi
    lines+=("$line")
done < "$file"

result=$(IFS=$'\n'; echo "${lines[*]}")
echo "$result" > $file

vhdl2vhdl=$(python3 hdlconv/vhdl2vhdl.py -h)
vhdl2vlog=$(python3 hdlconv/vhdl2vlog.py -h)
slog2vlog=$(python3 hdlconv/slog2vlog.py -h)

echo ""           >> $file
echo "$pattern"   >> $file
echo ""           >> $file

echo '```'        >> $file
echo "$vhdl2vhdl" >> $file
echo '```'        >> $file
echo ""           >> $file
echo '```'        >> $file
echo "$vhdl2vlog" >> $file
echo '```'        >> $file
echo ""           >> $file
echo '```'        >> $file
echo "$slog2vlog" >> $file
echo '```'        >> $file
