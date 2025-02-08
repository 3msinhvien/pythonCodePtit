from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd (a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def sumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

t = int(input())
for _ in range(t):
    a, b = map (int, input().split())
    if (isPrime(sumOfDigits(gcd(a, b)))):
        print("YES")
    else:
        print("NO")