def lamtron(n):
    k = 10
    while n >= k:
        r = n % k
        if r >= k // 2:
            n += k - r 
        else:
            n -= r 
        k *= 10 
    return n 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(lamtron(n))
