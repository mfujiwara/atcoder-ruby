MOD=998244353
N=int(input())
array=list(map(int,input().split()))
# ある値とaの組, 積の累積和をとるとaの値をとるindexまでの場合の数
stack=[(1,array[0])]
ret=array[0]
for a in array[1:]:
    tmp=-ret%MOD
    # 直前の値がa以下の分
    ret*=(1-a)
    ret%=MOD
    # 直前の値がaより大きい分
    while stack and stack[-1][1]>=a:
        x,y=stack.pop()
        tmp=(tmp+x)%MOD
        ret=(ret-x*(y-a))%MOD # 取りうる値がy-a、寄与度がx
    stack.append((tmp,a))
    #print(stack,ret)
if N%2==0:
    ret*=-1
print(ret%MOD)
