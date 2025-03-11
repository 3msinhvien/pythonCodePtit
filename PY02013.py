def count(n):
    myset = set()
    if n == 1:
        return 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
            myset.add(int(n))
        else:
            n = 3 * n + 1
            myset.add(n)
    return len(myset) + 1
while True:
    n = int(input())
    if n == 0:
        break
    print(count(n))