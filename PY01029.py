from math import gcd
def rev(n):
    res = 0 
    while ( n != 0 ):
        res = res * 10 + n % 10
        n = n // 10
    return res
t = int(input())
for _ in range(t):
    n = int(input())
    if (gcd(n, rev(n)) == 1):
        print("YES")
    else:
        print("NO")