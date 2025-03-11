from math import *
n = int(input())
list = list(map (int , input().split()))
list.sort()
for i in range (0 , n - 1):
    for j in range(i+1 , n):
        if ( list[i] != list[j] and gcd(list[i] , list[j]) == 1):
            print(list[i] , list[j])