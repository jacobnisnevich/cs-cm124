#!/usr/bin/env python

import sys

text = sys.stdin.read().strip()

numbers = text.split(" ")
sum_of_squares = int(numbers[0]) ** 2 + int(numbers[1]) ** 2

print(sum_of_squares)
