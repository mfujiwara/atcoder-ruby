import collections
S=input()
N=len(S)
INF=pow(10,10)
memo=collections.defaultdict(lambda: INF) # memo[i]:=ある状態での最小分割数（随時更新）
memo[0]=0
acc_bit=0
ord_a=ord("a")
for i in range(1,N+1):
    v=INF
    ch=ord(S[i-1])-ord_a
    acc_bit^=pow(2,ch)
    v=min(v,memo[acc_bit]+1)
    for j in range(26):
        v=min(v,memo[acc_bit^pow(2,j)]+1)
    memo[acc_bit]=min(memo[acc_bit],v)
print(v)
