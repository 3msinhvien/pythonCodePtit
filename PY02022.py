def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int (input())
my_dict = {}
list = list(map(int, input().split()))
for n in list:
    if ( n in my_dict):
        my_dict[n] += 1
    else:
        my_dict[n] = 1
for key in my_dict:
    if (isPrime(key)):
        print(key, my_dict[key])