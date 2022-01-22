H,W,K=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
a_sum=sum(a_array)
b_sum=sum(b_array)
if a_sum%K!=b_sum%K:
    print(-1)
    exit()
a_ret=0
for a in a_array:
    a_ret+=((K-1)*W-a+K)%K
b_ret=0
for b in b_array:
    b_ret+=((K-1)*H-b+K)%K
ret=max(a_ret,b_ret)
print((K-1)*H*W-ret)
