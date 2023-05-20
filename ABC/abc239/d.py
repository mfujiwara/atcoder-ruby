import math
def is_prime(n):
    if n==2: return True
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n+1):
        if n % i == 0:
            return False
    return True
A,B,C,D=map(int, input().split())
for x in range(A,B+1):
    enable=False
    for y in range(C,D+1):
        if is_prime(x+y):
            enable=True
            break
    if not enable:
        print("Takahashi")
        exit()
print("Aoki")
