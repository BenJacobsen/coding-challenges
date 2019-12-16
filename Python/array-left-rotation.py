import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    ret = []
    for count in range(0, len(a)):
        ret.append(a[(count + d) % len(a)])
    return ret
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
