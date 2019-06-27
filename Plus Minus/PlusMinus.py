#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr, n):
    ###Declarations
    pos = 0
    neg = 0
    zer = 0
    #Fractions
    neg_f = 0.0
    pos_f = 0.0
    zer_f = 0.0

    for i in range(len(arr)):
        if(arr[i] > 0):
            pos+=1
        if((arr[i]) < 0):
            neg+=1
        if (arr[i] == 0):
            zer += 1
    
    ###Setting Fractions for Print
    
    #Positive
    pos_f = (pos / n )
    #Negative
    neg_f = (neg / n )
    #Zero
    zer_f = (zer / n )
    ###Printing Fractions
    print(pos_f)
    print(neg_f)
    print(zer_f)


if __name__ == '__main__':
    n = int(input())
    
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
