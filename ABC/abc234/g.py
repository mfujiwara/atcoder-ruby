MOD=998244353
N=int(input())
array=list(map(int,input().split()))
# dp[i]:=先頭からi個使った時の答え
dp=[0]*(N+1)
dp[0]=1
# ある区間の最大値とその値に影響されるdpの値の総和の組、の配列
t_max=[]
# ある区間の最小値とその値に影響されるdpの値の総和の組、の配列
t_min=[]
# 最大値部分、最小値部分の累積
s_max=s_min=0
for i,a in enumerate(array):
    v_max=v_min=dp[i]
    # max
    while t_max and t_max[-1][0]<=a:
        # より大きい値が出てきたらそっちに寄せる
        x,y=t_max.pop()
        # 一旦マイナス
        s_max-=x*y%MOD
        s_max%=MOD
        # 影響するdpの値を累積
        v_max+=y
        v_max%=MOD
    s_max+=a*v_max%MOD
    s_max%=MOD
    t_max.append((a,v_max))
    # min
    while t_min and t_min[-1][0]>=a:
        x,y=t_min.pop()
        s_min-=x*y%MOD
        s_min%=MOD
        v_min+=y
        v_min%=MOD
    s_min+=a*v_min%MOD
    s_min%=MOD
    t_min.append((a,v_min))
    # dp
    dp[i+1]=(s_max-s_min)%MOD
print(dp[-1])
