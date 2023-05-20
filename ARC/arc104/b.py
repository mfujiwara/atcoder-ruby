N,S=input().split()
N=int(N)
ret=0
for i in range(N-1):
    counts=[0]*4
    for j in range(i,N):
        if S[j]=="A":
            counts[0]+=1
        elif S[j]=="T":
            counts[1]+=1
        elif S[j]=="C":
            counts[2]+=1
        else:
            counts[3]+=1
        if counts[0]==counts[1] and counts[2]==counts[3]:
            ret+=1
print(ret)
