#!/bin/bash

for f in `grep -r -l 0640 *`; do
  sed -i 's/0640/0640/g' $f
done
