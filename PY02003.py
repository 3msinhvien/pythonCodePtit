hamming = [1]
i2 = i3 = i5 = 0
max_val = 10**18
while True:
    ham = min(hamming[i2]*2, hamming[i3]*3, hamming[i5]*5)
    if ham <= max_val:
        hamming.append(ham)
        if ham == hamming[i2]*2:
            i2 += 1
        if ham == hamming[i3]*3:
            i3 += 1
        if ham == hamming[i5]*5:
            i5 += 1
    else: break        
t = int(input())
for i in range(t):
    a = int(input())
    if ( a in hamming):
       print(hamming.index(a)+1)
    else:
        print("Not in sequence")