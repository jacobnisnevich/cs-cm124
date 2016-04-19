#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

data = lines[0].strip()
k, m, n = map(int, data.split(" "))
total = k + m + n

probability = (k * (k - 1)) / (total * (total - 1)) + \
              (2 * k * m) / (total * (total - 1)) + \
              (2 * k * n) / (total * (total - 1)) + \
              (3 * m * (m - 1)) / (4 * total * (total - 1)) + \
              (n * m) / (total * (total - 1))

print(round(probability, 5))
