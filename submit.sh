#!/bin/bash

cat <<EOF | while read F; do echo cp $F DEST; done
Hello.txt
world.csv
EOF
echo "done"

