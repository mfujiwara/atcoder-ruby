def calc(b,n):
    ret=0
    while n>0:
        n,r=divmod(n,b)
        ret+=r
    return ret

n=int(input())
s=int(input())
if n==s:
    print(n+1)
    exit()
# 下から探索
for x in range(2,10**6):
    if calc(x,n)==s:
        print(x)
        exit()
# ここまでで見つからない場合、解があるならb進数で2桁
for p in range(10**6,0,-1):
    # 上位桁をpとする
    # n=p*b+(s-p)
    b=(n-s)//p+1
    if b>=2 and calc(b,n)==s:
        print(b)
        exit()  
print(-1)
