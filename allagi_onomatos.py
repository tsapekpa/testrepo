#!/usr/bin/env python3                                                         
import sys
import subprocess

with open(sys.argv[1]) as file:
  for line in file:
    k = line.strip()
    x = k.replace("jane","jdoe")
    subprocess.run(["mv", k, x])
                                                                     