#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

dna = lines[0].strip()

dictionary = {}
for char in dna:
	if char in dictionary:
		dictionary[char] += 1
	else:
		dictionary[char] = 1

print(str(dictionary['A']) + " " + 
	  str(dictionary['C']) + " " + 
	  str(dictionary['G']) + " " + 
	  str(dictionary['T']))
