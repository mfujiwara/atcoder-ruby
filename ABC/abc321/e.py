import sys
sys.setrecursionlimit(500000)
import math
T=int(input())
def child(n,x,k):
    if k<0:
        return 0
    if math.log2((n+x-1)/x)<k:
        return 0
    mini=x*pow(2,k)
    maxi=mini+pow(2,k)-1
    if n<mini:
        return 0
    elif maxi<=n:
        return pow(2,k)
    else:
        return n-mini+1
def parent(n,x,k):
    if x==1 or k==0:
        return 0
    if k==1:
        return 1
    if x%2==0:
        x2=x+1
    else:
        x2=x-1
    ret=child(n,x2,k-2)
    ret+=parent(n,x//2,k-1)
    return ret
rets=[]
for _ in range(T):
    N,X,K=map(int, input().split())
    ret=child(N,X,K)
    ret+=parent(N,X,K)
    rets.append(ret)
for ret in rets:
    print(ret)
