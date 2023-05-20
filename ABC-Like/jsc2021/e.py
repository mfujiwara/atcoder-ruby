import collections
K=int(input())
S=list(map(ord,list(input())))
targets=[(0,len(S),K)]
sss=[]
ccc=collections.defaultdict(list)
while targets:
    s,t,k=targets.pop()
    if k==0:
        if s+1==t:
            print("impossible")
            exit()
        elif s!=t:
            if len(sss)%2==0:
                sss.append(list(range(s,t)))
            else:
                sss.append(list(range(t-1,s-1,-1)))
    else:
        if s==t:
            print("impossible")
            exit()
        if (t-s)%2==0:
            l=(t-s)//2
            targets.append((s,s+l,k-1))
            targets.append((s+l,t,k-1))
        else:
            l=(t-s)//2
            targets.append((s,s+l,k-1))
            ccc[k].append(s+l)
            targets.append((s+l+1,t,k-1))
# print(sss)
# print(ccc)
ret=0
for k,array in ccc.items():
    total=len(array)
    counts=collections.defaultdict(int)
    for i in array:
        counts[S[i]]+=1
    ret+=total-max(counts.values())
if len(sss)==0:
    print(ret)
    exit()
parts=[]
diff=len(sss)
for i in range(len(sss[0])):
    total=len(sss)
    counts=collections.defaultdict(int)
    for array in sss:
        counts[S[array[i]]]+=1
    r1=(-1,-1)
    r2=(-2,-1)
    for w,c in counts.items():
        if c>=r1[0]:
            r1,r2=(c,w),r1
        elif c>=r2[0]:
            r2=(c,w)
    ret+=total-r1[0]
    parts.append(r1[1])
    if len(sss[0])%2==1 and i==len(sss[0])//2:
        continue
    if r2[0]>0:
        diff=min(diff,r1[0]-r2[0])
if parts==parts[::-1]:
    ret+=diff
print(ret)
