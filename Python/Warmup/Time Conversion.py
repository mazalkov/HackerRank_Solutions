# https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if (s[-2:] == "AM"):
        if (s[:2] == "12"):
            front = "00"
        else:
            return s[:-2]
    else:
        hour = int(s[:2])
        hour += 12
        if hour == 24:
            front = "12"
        else:
            front = str(hour)
            
    return front + s[2:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
