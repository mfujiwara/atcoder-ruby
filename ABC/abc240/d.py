N=int(input())
array=list(map(int, input().split()))
stack=[(0,0)]
ret=0
for a in array:
    if stack[-1][0]==a:
        _,n=stack.pop()
        if n==a-1:
            ret-=a-1
        else:
            stack.append((a,n+1))
            ret+=1
    else:
        stack.append((a,1))
        ret+=1
    print(ret)
