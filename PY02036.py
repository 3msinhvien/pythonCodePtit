from math import *

n = int(input())

myList = list(map(int , input().split()))
myList.sort()
for i in range ( 0 , len(myList) - 1 ):
    for j in range (i + 1 , len(myList)):
        if ( gcd(myList[i],myList[j]) == 1 ):
            print(myList[i] , myList[j])