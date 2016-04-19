#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

data = lines[0].strip().split(" ")
chance_dominant = [1, 1, 1, 0.75, 0.5, 0]

expected_value = 0
for i in range(0, 5):
	expected_value += float(data[i]) * chance_dominant[i] * 2

print(expected_value)
