import collections
N=int(input())
S=input()
T=input()
if S.count("0")%2!=T.count("0")%2:
    print(-1)
    exit()
ret=0
s_queue=collections.deque()
t_queue=collections.deque()
for i in range(N):
    s=0 if S[i]=="0" else 1
    t=0 if T[i]=="0" else 1
    if s_queue and s==1:
        ret+=i-s_queue.pop()
        s=0
    if t_queue and s==1:
        ret+=i-t_queue.popleft()
        s=0
    if s==0:
        if t==1:
            t_queue.append(i)
        else:
            continue
    elif s==1:
        if t==0:
            s_queue.append(i)
        else:
            continue
if s_queue or t_queue:
    print(-1)
else:    
    print(ret)
