#!/bin/python3
#https://www.hackerrank.com/challenges/compare-the-triplets/problem
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    x = y = 0
    for i in range(0, 3):
        x = x + int(a[i] - b[i] > 0)
        y = y + int(b[i] - a[i] > 0)
    return [x, y]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
