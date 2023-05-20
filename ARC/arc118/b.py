import collections
K,N,M=map(int, input().split())
array=[] #(index, a*M, mod N)
for i,a in enumerate(list(map(int, input().split()))):
    v=a*M
    array.append((i,v,v%N))
array=collections.deque(sorted(array, key=lambda e: e[2]))
rets=[]
diff=0
while array:
    left=array[0]
    right=array[-1]
    if left[2]+diff<=N-right[2]:
        rets.append((left[0],(left[1]-left[2])//N))
        array.popleft()
        diff+=left[2]
    else:
        rets.append((right[0],(right[1]+N-right[2])//N))
        array.pop()
        diff-=N-right[2]
rets=sorted(rets)
str_rets=[str(a) for i,a in rets]
print(" ".join(str_rets))
