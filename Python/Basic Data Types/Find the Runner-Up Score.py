# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
# converting to a list because why is it a map??    
new_arr = list(arr)

# then convert the list to a set to remove duplicates
new_arr = set(new_arr)

# remove the max element to get the second highest
new_arr.remove(max(new_arr))
print(max(new_arr))
