N=int(input())
ab=[]
time=0
for _ in range(N):
    a,b=map(int, input().split())
    ab.append((a,b))
    time+=a/b
ret=0
time/=2
for i in range(N):
    a,b=ab[i]
    if time>a/b:
        time-=a/b
        ret+=a
    else:
        ret+=time*b
        break
print(ret)
