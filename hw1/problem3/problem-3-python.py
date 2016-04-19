#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

bounds = lines[0].split(" ")
bound_1 = int(bounds[0])
bound_2 = int(bounds[1])

sum = 0

for i in range(bound_1, bound_2):
	if i % 2 == 1:
		sum += i

print(sum)
