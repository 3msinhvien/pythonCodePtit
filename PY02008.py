import math
def eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Trả về danh sách các số nguyên tố
    return [i for i in range(limit + 1) if is_prime[i]]
    
prime = eratosthenes(10000)
n , x = map(int , input().split())
print(x, end=" ")
cur = x 
for i in range (1 , n + 1):
    cur += prime[i-1]
    print(cur, end=" ")