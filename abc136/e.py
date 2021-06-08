import collections
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
def judge(arr, k ,mod):
    for i in range(len(arr)):
        arr[i]%=mod
    arr=collections.deque(sorted(arr))
    while len(arr)>0 and arr[0]==0:
        arr.popleft()
    cost=0
    stack=0
    while arr:
        if stack==0:
            if arr[0]<=mod-arr[-1]:
                a=arr.popleft()
                stack-=a
                cost+=a
            else:
                a=arr.pop()
                stack+=(mod-a)
                cost+=(mod-a)
        elif stack>0:
            a=arr.popleft()
            stack-=a
            cost+=a
        else:
            a=arr.pop()
            stack+=(mod-a)
            cost+=(mod-a)
    if cost//2<=k:
        return True
    else:
        return False
N,K=map(int, input().split())
array=list(map(int, input().split()))
divisors=make_divisors(sum(array))
for divisor in divisors[::-1]:
    if judge(array[:],K,divisor):
        print(divisor)
        exit()
