N=int(input())
lefts=[]
rights=[]
for i in range(N):
    l,r=map(int, input().split())
    lefts.append(l)
    rights.append(-r)
lefts.sort()
rights.sort()
ret=0
total=0
for i in range(N):
    l=lefts.pop()
    r=rights.pop()
    ret=max(ret,total+l,total+r,total+r+l)
    total+=l+r
print(ret*2)
