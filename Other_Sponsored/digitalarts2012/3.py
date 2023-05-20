N,M,K=map(int, input().split())
counts=[0]*N
plus=[0]*N
ff={}
for _ in range(M):
    s=input().split()
    if s[0]=="t":
        j=int(s[1])-1
        counts[j]+=1
    elif s[0]=="f":
        j=int(s[1])-1
        k=int(s[2])-1
        if j>k:
            j,k=k,j
        if (j,k) in ff:
            continue
        ff[(j,k)]=(counts[j],counts[k])
    else:
        j=int(s[1])-1
        k=int(s[2])-1
        if j>k:
            j,k=k,j
        if (j,k) not in ff:
            continue
        jc,kc=ff.pop((j,k))
        plus[j]+=counts[k]-kc
        plus[k]+=counts[j]-jc
for key in ff:
    j,k=key
    jc,kc=ff[key]
    plus[j]+=counts[k]-kc
    plus[k]+=counts[j]-jc
for i in range(N):
    counts[i]+=plus[i]
counts.sort(reverse=True)
print(counts[K-1])
