#!/bin/python3

# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import sys


def calc_sum(k):
    n3 = (k-1) // 3
    n5 = (k-1) // 5
    n15 = (k-1) // 15
    sum = (3 * (n3 + 1) * n3 // 2) + (5 * (n5 + 1) * n5 // 2) - (15 * (n15 + 1) * n15 // 2)
    return sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = calc_sum(n)
    # sum = 0
    # for i in range(1, n, 1):
    #     if (i % 3 == 0 or i % 5 == 0):
    #         sum += i
    print(sum)
