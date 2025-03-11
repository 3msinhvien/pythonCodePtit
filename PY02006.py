t = int (input())
for i in range (0, t):
    n = int (input())
    arr1 = list(map(int , input().split()))
    arr2 = list(map(int, input().split()))
    arr1.sort()
    arr2.sort()
    check = 1
    for i in range (0 , n):
        # print(arr1[i])
        if ( arr1[i] > arr2[i]): check = 0
    if check == 1: print("YES")
    else: print("NO") 