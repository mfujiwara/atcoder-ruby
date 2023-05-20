N=int(input())
array=list(map(int, input().split()))
xor_total=0
for a in array:
    xor_total^=a
base=[]
for a in array:
    a&=~xor_total # 行標準形？
    for e in base:
        a = min(a,a^e)
    if a>0:
        base.append(a)
xor_a=0
for e in base:
    xor_a=max(xor_a,xor_a^e)
xor_b=xor_total^xor_a
print(xor_a+xor_b)
