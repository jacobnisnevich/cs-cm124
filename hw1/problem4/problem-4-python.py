#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

index = 1
for line in lines:
	if index % 2 == 0:
		print(line, end="")
	index += 1
