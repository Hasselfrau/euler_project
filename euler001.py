#!/bin/python3

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
