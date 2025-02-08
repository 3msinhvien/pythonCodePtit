equation = input()
a , operator , b , equal_sign , c  = equation.split()
a = int(a)
b = int(b)
c = int(c)
if operator =='+':
    if a+b == c:
        print('YES')
    else:
        print('NO')
elif operator =='-':
    if a-b == c:
        print('YES')
    else:
        print('NO')
elif operator =='*':
    if a*b == c:
        print('YES')
    else:
        print('NO')
else:
    if a/b == c:
        print('YES')
    else:
        print('NO')