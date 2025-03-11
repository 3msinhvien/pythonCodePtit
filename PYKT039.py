t = int (input())
for _ in range(t):
    n = int(input())
    a = list( map ( int , input().split()))
    b = list(map (int , input().split()))
    a.sort()
    b.sort()
    check = 0 
    for i in range ( 0 , len(a)):
        if ( a[i] > b[i]):
            check = 1
    if ( check == 1 ):
        print("NO")
    else:
        print("YES")    