def solve(a , k , n):
    check = 0 
    i = 1
    while (k * i <= n):
        if (k * i - a > 0):
            print(k * i - a , end = " ")
            check = 1
        i += 1
    if ( check == 0 ): print(-1)


a , k , n = map (int, input().split())
solve(a , k , n)