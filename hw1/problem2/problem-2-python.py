#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

string = lines[0]
indices = lines[1].split(" ")

word_1 = string[int(indices[0]):int(indices[1]) + 1]
word_2 = string[int(indices[2]):int(indices[3]) + 1]

print(word_1 + " " + word_2)
