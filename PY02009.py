from collections import Counter

t = int(input())
for _ in range(t):
    arr = [0] * 10000
    most_common = 0 
    n = int(input())
    for _ in range(n):
        number = int (input())
        arr[number] += 1
        most_common = max(most_common, arr[number])
    print(arr.index(most_common))   