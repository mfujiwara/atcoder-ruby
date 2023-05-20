import bisect
N,Q=map(int, input().split())
array=list(map(int, input().split()))
array.sort()
dic={}
for i,a in enumerate(array):
    dic[a]=i
memo=[sum(array)-array[0]*N]
for i in range(1,N):
    d=array[i]-array[i-1]
    memo.append(memo[-1]+d*i-d*(N-i))
# print(array)
# print(memo)
for _ in range(Q):
    x=int(input())
    if x in dic:
        print(memo[dic[x]])
    elif x<array[0]:
        print(memo[0]+(array[0]-x)*N)
    elif x>array[-1]:
        print(memo[-1]+(x-array[-1])*N)
    else:
        index=bisect.bisect(array,x)
        p=array[index]-x
        q=x-array[index-1]
        d=memo[index]-memo[index-1]
        ret=memo[index-1]+d*q//(p+q)
        print(ret)

