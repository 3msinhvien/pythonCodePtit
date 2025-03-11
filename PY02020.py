n = int (input())
list = list(map(float , input().split()))
maxVal = max(list)
minVal = min(list)
cnt = 0 
sum = 0
for i in list:
    if i != maxVal and i != minVal:
        cnt += 1
        sum += i
print(f"{sum/cnt:.2f}") 