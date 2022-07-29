import collections
N=int(input())
array=list(map(int, input().split()))
array.sort(reverse=True)
ret=0
stack=collections.deque()
for a in array:
    if stack:
        b,c=stack.pop()
        ret+=b
        if c>0:
            stack.append((b,c-1))
        stack.appendleft((a,1))
    else:
        stack.appendleft((a,0))
    #print(ret)
print(ret)
