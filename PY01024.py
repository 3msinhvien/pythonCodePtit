from math import *
def check(n):
    sum_digit = 0 
    for i in str(n):
        sum_digit += int(i)
    if sum_digit % 10 != 0:
        return False
    for i in range(2, len(str(n))):
        if (abs(ord(str(n)[i]) - ord(str(n)[i - 1])) != 2):
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if (check(n) == True):
        print('YES')
    else:  print('NO')