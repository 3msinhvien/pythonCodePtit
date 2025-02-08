def palindrome(s):
    return s == s[::-1]
def check(s):
    for i in s:
        if i != '2' and i != '4' and i != '6' and i != '8':
            return False
    if s.len() % 2 != 1:
        return False
t = input()
for _ in range(t):
        n = input()
        for i in range(n):
            s = raw_input()
            if check(s) and palindrome(s):
                print "YES"
            else:
                print "NO"