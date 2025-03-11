from functools import cmp_to_key
def sumdigit(n):
    return sum([int(i) for i in str(n)])

def cmp ( a , b):
    if (sumdigit(a) == sumdigit(b)):
        return a - b 
    if (sumdigit(a) < sumdigit(b)):
        return -1
    else: return 1
    
t = int(input())
for _ in range (t):
    n = int(input())
    my_list = list(map(int , input().split()))
    my_list.sort(key = cmp_to_key(cmp))
    for i in my_list:
        print(i, end = " ")
    print()