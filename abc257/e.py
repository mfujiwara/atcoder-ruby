N=int(input())
array=list(map(int, input().split()))
mini=min(array)
q,r=divmod(N,mini)
rets=[0]*9
for i in range(8,-1,-1):
    if array[i]==mini:
        print(str(i+1)*q)
        break
    else:
        t=r//(array[i]-mini)
        if t>0:
            print(str(i+1)*t,end="")
            q-=t
            r-=t*(array[i]-mini)
