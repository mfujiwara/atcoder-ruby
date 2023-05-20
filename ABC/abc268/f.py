INF=pow(10,20)
N=int(input())
memo=[]
for _ in range(N):
    s=input()
    x_count=0
    total=0
    for ch in s:
        if ch=="X":
            x_count+=1
        else:
            total+=int(ch)
    # (x,t)が前にあった場合 x*total
    # (x,t)が後にあった場合 t*x_count
    if x_count==0:
        memo.append((INF,s))
    else:
        memo.append((total/x_count,s))
memo.sort()
ret=0
x_count=0
for _,s in memo:
    for ch in s:
        if ch=="X":
            x_count+=1
        else:
            ret+=x_count*int(ch)
print(ret)
