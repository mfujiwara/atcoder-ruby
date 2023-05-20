X=input()
x_map={}
for i,ch in enumerate(X):
    x_map[ch]=i
N=int(input())
names=[]
for _ in range(N):
    name=input()
    n=[]
    for ch in name:
        n.append(x_map[ch])
    names.append(n)
names.sort()
for name in names:
    r=[]
    for v in name:
        r.append(X[v])
    print("".join(r))
