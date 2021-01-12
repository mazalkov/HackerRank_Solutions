# https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    
    pos_count = 0
    neg_count = 0
    zero_count = 0
    
    for elem in arr:
        if elem > 0:
            pos_count += 1
        
        elif elem < 0:
            neg_count += 1
        
        else:
            zero_count += 1
            
    print(pos_count/n, "\n", neg_count/n, "\n", zero_count/n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
