#!/usr/bin/env Rscript

f <- file("stdin")
open(f)
text <- readLines(f, n = 1)

numbers = strsplit(text, " ")[[1]]
sum_of_squares = as.integer(numbers[1])^2 + as.integer(numbers[2])^2

write(sum_of_squares, stdout())
