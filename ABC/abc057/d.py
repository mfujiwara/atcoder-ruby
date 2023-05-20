import bisect
fact=[1]
for i in range(1,51):
    fact.append(fact[-1]*i)
N,A,B=map(int, input().split())
array=sorted(list(map(int, input().split())))
v=array[-A]
count=array.count(v)
other=N-bisect.bisect_right(array,v)
ret=0
if other==0:
    for i in range(A-other,min(B-other,count)+1):
        ret+=fact[count]//fact[count-i]//fact[i]
else:
    ret=fact[count]//fact[count-A+other]//fact[A-other]
print(sum(array[-A:])/A)
print(ret)
