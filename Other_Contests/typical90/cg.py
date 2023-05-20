import collections
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
K=int(input())
counts=collections.Counter(prime_factorize(K))
total=[1,0,0] # total[i]:=3つのグループに分けたときに異なる数がi+1種類の数が出てくる場合の数
for c in counts.values():
    t=[0,0,0]
    for i in range(c+1):
        for j in range(c+1-i):
            k=c-i-j
            if i==j==k:
                t[0]+=1
            elif i==j or j==k or k==i:
                t[1]+=1
            else:
                t[2]+=1
    t[1]//=3
    t[2]//=6
    total=[
        total[0]*t[0],
        total[0]*t[1] +total[1]*t[0]+total[1]*t[1],
        total[0]*t[2] +total[1]*(t[1]+t[2]*3) +total[2]*(t[0]+t[1]*3+t[2]*6)
        ]
print(sum(total))
