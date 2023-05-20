import math
N,M=map(int, input().split())
S=input()
T=input()
g=math.gcd(N,M)
l=N*M//g
x={}
for i,ch in enumerate(S):
    x[l//N*i]=ord(ch)
for i,ch in enumerate(T):
    k=l//M*i
    if k in x and x[k]!=0 and x[k]!=ord(ch):
        print(-1)
        exit()
print(l)
