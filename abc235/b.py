N=int(input())
array=list(map(int, input().split()))
now=array[0]
for i in range(1,N):
    if now<array[i]:
        now=array[i]
    else:
        break
print(now)
