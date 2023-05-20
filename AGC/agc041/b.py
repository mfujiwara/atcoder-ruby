N,M,V,P=map(int, input().split())
array=list(map(int, input().split()))
array=sorted(array)
sums=[0]
for a in array:
    sums.append(sums[-1]+a)
sums=sums[1:]
# minimum check
v=array[0]+M
if V<=P:
    if v>=array[-P]:
        print(N)
        exit()
else:
    if v>=array[-P]:
        # 1..N-P を v にするのに必要な数
        total=v*(N-P)
        base=sums[N-P]-sums[0]
        need=total-base
        # 出せる数
        enable=(V-P)*M
        if need>=enable:
            print(N)
            exit()
right=0
left=N-P
while True:
    if right+1==left:
        print(N-left)
        exit()
    mid=(right+left)//2
    v=array[mid]+M
    if V<=P:
        if v>=array[-P]:
            left=mid
        else:
            right=mid
    else:
        if v>=array[-P]:
            # mid+1..N-Pを v にするのに必要な数
            total=v*(N-P-mid)
            base=sums[N-P]-sums[mid]
            need=total-base
            # 出せる数
            enable=max(0,V-P-mid)*M
            if need>=enable:
                left=mid
            else:
                right=mid
        else:
            right=mid
