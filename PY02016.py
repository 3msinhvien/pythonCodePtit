from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    counter = Counter(input().split())
    if int (max(counter, key=counter.get)) >= int(n/2):
        print(max(counter, key=counter.get))
    else:
        print('NO')