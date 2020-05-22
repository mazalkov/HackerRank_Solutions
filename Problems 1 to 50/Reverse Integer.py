# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = x[::-1] 
        return int(x)
