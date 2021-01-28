# https://www.hackerrank.com/challenges/list-comprehensions/


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
permutations = []

# added 1 to x,y,z indices because of Python's inclusive-exclusive range
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            # if the sum is n, go to next item
            if i+j+k == n:
                next
            else:
                # otherwise append the combination
                permutations.append([i, j, k])
            

print(permutations)
