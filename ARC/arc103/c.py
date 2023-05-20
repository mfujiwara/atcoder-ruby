s=input()
array=list(map(int,list(s)))
if array[0]==0 or array.pop()!=0:
    print(-1)
    exit()
N=len(array)+1
for i in range(N//2):
    if array[i]!=array[-1-i]:
        print(-1)
        exit()
parents=[N-1]
for i in range(N-2,-1,-1):
    if array[i]==1:
        parents.append(i)
for i in range(N-1):
    if i==parents[-1]:
        parents.pop()
    print(f"{parents[-1]+1} {i+1}")
