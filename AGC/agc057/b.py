N,X=map(int, input().split())
array=list(map(int, input().split()))
MAX=max(array)
memo=[]
# それぞれの要素をMAXに近づける
for a in array:
    mini=a
    maxi=a
    while maxi<MAX:
        mini=mini*2
        maxi=maxi*2+X
    if mini<=MAX:
        memo.append((MAX,MAX))
    else:
        memo.append(((maxi-X)//2,mini))
memo.sort()
ret=MAX
m=MAX
for low,up in memo:
    # 最小値をlowにした場合を考える（すると、配列の後側はlow以上m以下を取れる）
    ret=min(ret,m-low)
    # 繰り返しで同じ考え方をした時に最小をとらなくする必要があるので、mに吸収
    m=max(m,up)
if ret<X:
    print(0)
else:
    print(ret)
