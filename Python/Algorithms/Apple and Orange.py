# https://www.hackerrank.com/challenges/apple-and-orange/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    sum_apples = 0
    sum_oranges = 0
    
    for distance in apples:
        distance += a
        if s <= distance <= t:
            sum_apples += 1
        
    for distance in oranges:
        distance += b
        if s <= distance <= t:
            sum_oranges += 1
            
    print(sum_apples)
    print(sum_oranges)
        
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
