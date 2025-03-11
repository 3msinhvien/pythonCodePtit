f = [1 , 1 , 2]
for i in range (3 , 100):
    f.append( f[i-1] + f[i-2])
t = int(input())
for _ in range (t):
    a, b = map(int , input().split())
    for i in range (a - 1 , b):
        print(f[i] , end = " ")
    print()