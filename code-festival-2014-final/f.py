import math
N=int(input())
B=[int(input()) for _ in range(N)]
bools=[]
for i in range(N):
    b1=B[i]
    b2=B[(i+1)%N]
    b3=B[(i+2)%N]
    if b2%math.gcd(b1,b3)==0:
        bools.append(True)
    else:
        bools.append(False)
ret1=0
i=0
while i<N:
    if not bools[i]:
        ret1+=1
        i+=3
    else:
        i+=1
ret2=0
i=1
while i<N+1:
    if not bools[i%N]:
        ret2+=1
        i+=3
    else:
        i+=1
ret3=0
i=2
while i<N+2:
    if not bools[i%N]:
        ret3+=1
        i+=3
    else:
        i+=1
print(min(ret1,ret2,ret3))
