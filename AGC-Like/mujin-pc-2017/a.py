MOD=pow(10,9)+7
N=int(input())
array=list(map(int, input().split()))[::-1]
ret=1
stack=0
while array:
    if array[-1]==stack*2:
        ret*=(stack+1)
        ret%=MOD
        array.pop()
    elif array[-1]>stack*2:
        array.pop()
        stack+=1
    else:
        ret*=stack
        ret%=MOD
        stack-=1
while stack>1:
    ret*=stack
    ret%=MOD
    stack-=1
print(ret)
