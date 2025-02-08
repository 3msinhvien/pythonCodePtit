def decode(s):
    res = ''
    for i in range(0, len(s), 2):
        res += s[i] * int(s[i+1])
    return res
t = int(input())
for _ in range(t):
    s = input()
    print(decode(s))