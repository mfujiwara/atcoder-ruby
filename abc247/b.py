import collections
N=int(input())
counts=collections.defaultdict(int)
st=[]
for _ in range(N):
    s,t=input().split()
    st.append((s,t))
    counts[s]+=1
    if s!=t:
        counts[t]+=1
for s,t in st:
    if counts[s]>1 and counts[t]>1:
        print("No")
        exit()
print("Yes")
