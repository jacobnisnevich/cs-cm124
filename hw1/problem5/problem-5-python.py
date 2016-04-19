#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

words = lines[0].strip().split(" ")

dictionary = {}
for word in words:
	if word in dictionary:
		dictionary[word] += 1
	else:
		dictionary[word] = 1

for key, value in dictionary.items():
	print(key + " " + str(value))
