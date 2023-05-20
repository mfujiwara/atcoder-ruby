N,L=map(int, input().split())
r_stack=[0,0]
l_stack=[0,0]
ret=0
for _ in range(N):
    x,d=input().split()
    x=int(x)
    if d=="L":
        if l_stack[1]==0:
            l_stack=[x,1]
        else:
            ret+=x-l_stack[0]-l_stack[1]
            l_stack[1]+=1
    else:
        if l_stack[1]==0:
            if r_stack[1]==0:
                r_stack=[x,1]
            else:
                ret+=(x-r_stack[0]-1)*r_stack[1]
                r_stack[0]=x
                r_stack[1]+=1
        else:
            ret+=(l_stack[0]-r_stack[0]-1)*max(r_stack[1],l_stack[1])
            l_stack=[0,0]
            r_stack=[x,1]
if r_stack[1]==0:
    r_stack[1]=1
elif l_stack[1]==0:
    l_stack=[L+1,1]
ret+=(l_stack[0]-r_stack[0]-1)*max(r_stack[1],l_stack[1])
print(ret)
