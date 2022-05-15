N=int(input())
done=set()
ret=(-1,-1)
for i in range(N):
    s,t=input().split()
    t=int(t)
    if s not in done:
        done.add(s)
        if t>ret[0]:
            ret=(t,i+1)
print(ret[1])
