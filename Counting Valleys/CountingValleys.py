#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(n, s):
#initialization
    level = 0
    valley = 0

#Vally Counter Loop
    for i in range(n):
        if (s[i]=='U'):
            level += 1
            if level == 0:
                valley += 1
        else:
            level -= 1
    return valley

#Pre-Written (Handles Input)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
