N,W=map(int, input().split())
ab=[]
for _ in range(N):
    a,b=map(int, input().split())
    ab.append((a,b))
ab.sort()
ret=0
while W>0 and ab:
    a,b=ab.pop()
    if W>=b:
        ret+=a*b
        W-=b
    else:
        ret+=a*W
        W=0
print(ret)
