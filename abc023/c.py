import collections
R,C,K=map(int, input().split())
N=int(input())
candies=set()
r_candies=[0]*R
c_candies=[0]*C
for _ in range(N):
    r,c=map(int, input().split())
    r-=1
    c-=1
    candies.add((r,c))
    r_candies[r]+=1
    c_candies[c]+=1
num2r=collections.defaultdict(list)
num2c=collections.defaultdict(list)
for i,v in enumerate(r_candies):
    num2r[v].append(i)
for i,v in enumerate(c_candies):
    num2c[v].append(i)
ret=0
for num_r in num2r:
    num_c=K-num_r
    if num_c>=0:
        ret+=len(num2r[num_r])*len(num2c[num_c])
for r,c in candies:
    v=r_candies[r]+c_candies[c]
    if v==K:
        ret-=1
    elif v==K+1:
        ret+=1
print(ret)
