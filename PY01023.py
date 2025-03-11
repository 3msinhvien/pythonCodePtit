from math import sqrt
t = int (input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    else:
        factor = []
        print('1 * ', end = '')
        for i in range(2, int(sqrt(n)) + 1):
            mu = 0
            while n % i == 0:
                mu += 1
                n //= i 
            if mu >= 1:
                factor.append(f"{i}^{mu}")
        if n > 1:    
            factor.append(f"{n}^1")
        print(' * '.join(factor))