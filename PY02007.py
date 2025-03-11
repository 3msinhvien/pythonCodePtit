myset = set()
arr = [int(x) for x in input().split()] 
x = 0 
for i in arr:
    myset.add( i % 42)
    x += 1
    if ( x == 10 ): break
print(len(myset))