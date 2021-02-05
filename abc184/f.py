import bisect
N,T=map(int, input().split())
array=list(map(int, input().split()))
memo1={0}
for a in array[:N//2]:
    if a>T:
        continue
    for b in list(memo1):
        c=a+b
        if c<=T:
            memo1.add(c)
    memo1.add(a)
list1=sorted(list(memo1))
memo2={0}
for a in array[N//2:]:
    if a>T:
        continue
    for b in list(memo2):
        c=a+b
        if c<=T:
            memo2.add(c)
    memo2.add(a)
list2=sorted(list(memo2))
ret=0
for a in list1:
    b=list2[bisect.bisect_right(list2,T-a)-1]
    ret=max(ret,a+b)
print(ret)
