# https://www.hackerrank.com/challenges/string-validators/


if __name__ == '__main__':
    s = input()
    
    
print(any([character.isalnum() for character in s]))
print(any([character.isalpha() for character in s]))
print(any([character.isdigit() for character in s]))
print(any([character.islower() for character in s]))
print(any([character.isupper() for character in s]))
