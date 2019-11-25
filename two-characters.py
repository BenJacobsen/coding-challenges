#!/bin/python3
#https://www.hackerrank.com/challenges/two-characters/problem
import math
import os
import random
import re
import sys

def recurse(str, set):
    if len(set) < 2:
        return 0
    for i in range(0, len(str)-1):
        if str[i] == str[i+1]:
            return recurse(str.replace(str[i], ''), set.replace(str[i], ''))
    if len(set) == 2:
        return len(str)
    high = 0
    for char in set:
        high = max(high, recurse(str.replace(char, ''), set.replace(char, '')))
    return high

# Complete the alternate function below.
def alternate(str):
    set = str[0]
    for char in str:
        if set.find(char) == -1:
            set += char
    return recurse(str, set)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
