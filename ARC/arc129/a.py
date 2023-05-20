N,L,R=map(int, input().split())
left=1
right=1
ret=0
while left<=N:
    if N&left!=0 and right>=L and R>=left:
        ret+=min(right,R)-max(left,L)+1
    left*=2
    right*=2
    right+=1
print(ret)
