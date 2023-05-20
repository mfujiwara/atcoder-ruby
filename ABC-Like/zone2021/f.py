N,M=map(int, input().split())
array=list(map(int, input().split()))
memo=[True]*N
for a in array:
    memo[a]=False
# arrayに含まれていない集合のxorの基底を求める
base=[]
elim=[]
for x in range(1, N):
    if not memo[x]:
        continue
    y=x
    for b in elim:
        y = min(y, y ^ b)
    if y:
        base.append(x)
        elim.append(y)
def lg(x):
    return x.bit_length() - 1
# 基底がn-1要素に満たない場合は不可(N=2^n)
if len(base)<lg(N):
    print(-1)
    exit()
# グレイコードの容量でN-1要素求める
xor=0
for x in range(1, N):
    next=xor^base[lg(x & -x)]
    print(xor,next)
    xor=next
