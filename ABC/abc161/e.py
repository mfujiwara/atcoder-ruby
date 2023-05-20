N,K,C=map(int, input().split())
S=input()
ret1=[]
pre=-C-1
for i in range(N):
    if S[i]=="o" and pre+C<i:
        ret1.append(i)
        pre=i
        if len(ret1)==K:
            break
ret2=[]
pre=N+C
for i in range(N-1,-1,-1):
    if S[i]=="o" and pre-C>i:
        ret2.append(i)
        pre=i
        if len(ret2)==K:
            break
i1=0
i2=K-1
rets=[]
while i1<K and i2>=0:
    if ret1[i1]==ret2[i2]:
        rets.append(ret1[i1])
        i1+=1
        i2-=1
    elif ret1[i1]>ret2[i2]:
        i2-=1
    else:
        i1+=1
ret3=[]
pre=-C-1
rets_set=set(rets)
for i in range(N):
    if S[i]=="o" and pre+C<i and i not in rets_set:
        ret3.append(i)
        pre=i
        if len(ret3)==K:
            exit()
for r in rets:
    print(r+1)
