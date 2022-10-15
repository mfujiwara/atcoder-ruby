N=int(input())
array=list(map(int, input().split()))
evens=[]
odds=[]
for a in array:
    if a%2==0:
        evens.append(a)
    else:
        odds.append(a)
evens.sort()
odds.sort()
ret=-1
if len(evens)>=2:
    ret=max(ret,evens[-1]+evens[-2])
if len(odds)>=2:
    ret=max(ret,odds[-1]+odds[-2])
print(ret)
