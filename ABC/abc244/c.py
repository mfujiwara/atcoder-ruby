
N=int(input())
s=set([i+1 for i in range(2*N+1)])
while s:
    print(s.pop(), flush=True)
    t=int(input())
    if t==0:
        break
    s.remove(t)
