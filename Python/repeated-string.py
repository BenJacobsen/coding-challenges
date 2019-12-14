#https://www.hackerrank.com/challenges/repeated-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    remainder = n % len(s)
    remainderA = totalA = 0
    for count,char in enumerate(s):
        if char == 'a':
            if count < remainder:
                remainderA += 1
            totalA += 1
    return remainderA + (totalA * (n // len(s)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
