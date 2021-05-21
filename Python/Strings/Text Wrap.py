# https://www.hackerrank.com/challenges/text-wrap/


import textwrap

def wrap(string, max_width):
    
    wraps = textwrap.fill(string, max_width)
    
    return wraps

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
