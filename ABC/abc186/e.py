def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0
T=int(input())
for _ in range(T):
    N,S,K=map(int, input().split())
    R=N-S
    # yN + Kx = d
    d,x,y=extgcd(K,N)
    if R%d!=0:
        print(-1)
        continue
    K//=d
    N//=d
    R//=d
    # Kx + Ny = 1 => KRx + NRy = R
    r = (R*x % N + N) % N
    print(abs(r))
