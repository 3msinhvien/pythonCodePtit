n = int (input())
list = [0] * 1000001
for _ in range(n):
    list[int(input())] = 1
for i in range(1000001):
    if list[i] == 0 and i != 0:
        print(i)
        break
