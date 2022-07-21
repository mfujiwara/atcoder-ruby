A,B,C=sorted(map(int, input().split()))
ret=C-B
A-=ret
ret+=B-A
if A>=0:
    print(ret+A)
else:
    print(-1)
