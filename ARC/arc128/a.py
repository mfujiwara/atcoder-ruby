N=int(input())
array=list(map(int, input().split()))
array.append(pow(10,10))
rets=[0]*N
stack=[(-1,0)]
for i,a in enumerate(array):
    if len(stack)==1:
        if a>stack[0][1]:
            stack[0]=(i,a)
        elif a<stack[0][1]:
            stack.append((i,a))
    elif len(stack)==2:
        if a<stack[1][1]:
            stack[1]=(i,a)
        elif a>stack[1][1]:
            for j,_ in stack:
                rets[j]=1
            stack=[(i,a)]
print(*rets)
