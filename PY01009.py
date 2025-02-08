s = input()
cnt = 0 
for i in s:
    if i.islower():
        cnt += 1
    else:
        cnt -= 1
if cnt >=0:
    print(s.lower())
else:
    print(s.upper())