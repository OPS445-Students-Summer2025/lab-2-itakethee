#!/usr/bin/env python3
import sys
# Author: Purav Shah
# Author ID: pshah116
# Date Created: Tuesday May 20,2025

if len(sys.argv) == 2:
    count = int(sys.argv[1])
else:
    count = 3

while count > 0:
    print(count)
    count -= 1

print("blast off!")
