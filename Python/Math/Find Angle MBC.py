# https://www.hackerrank.com/challenges/find-angle/


# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


AB = input()
BC = input()

theta = math.degrees(math.atan(int(AB)/int(BC)))

print(str(round(theta)) + u'\u00B0')
