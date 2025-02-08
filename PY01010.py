def check(s):
    if s[0] != s[-2] or s[1] != s[-1]:
        return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")