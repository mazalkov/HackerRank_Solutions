# https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for row in range(n):
        print((" " * (n-row-1)) + ("#" * (row+1)))
    
if __name__ == '__main__':
    n = int(input())

    staircase(n)
