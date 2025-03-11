from functools import cmp_to_key

def multi_digit (n):
    res = 1
    for i in str(n):
        res *= int(i)
    return res

def cmp ( a , b):
    if multi_digit(a) == multi_digit(b):
        return (a - b)
    else:
        return multi_digit(a) - multi_digit(b)
t = int(input())
my_list = []
for _ in range(t):
    n = int(input())
    my_list = list(map(int, input().split()))
    my_list.sort(key= cmp_to_key(cmp))
    for i in my_list:
        print(i, end=' ')
    print()