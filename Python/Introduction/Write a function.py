# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        return True
    else:
        return not (year % 100 == 0) and (year % 4 == 0)
    
    return leap

year = int(input())
