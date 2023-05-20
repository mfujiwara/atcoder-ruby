N=int(input())
dots=[]
for i in range(N):
    x,y=map(int, input().split())
    dots.append((x,y))
M=int(input())
ops=[(1,0,0,0,1,0,0,0,1)]
for _ in range(M):
    # a,b,c
    # d,e,f
    # g,h,i
    op=list(map(int, input().split()))
    if op[0]==1:
        a,b,c,d,e,f,g,h,i=ops[-1]
        # 0,1,0
        #-1,0,0
        # 0,0,1
        ops.append((d,e,f,-1*a,-1*b,-1*c,g,h,i))
    elif op[0]==2:
        a,b,c,d,e,f,g,h,i=ops[-1]
        # 0,-1,0
        # 1,0,0
        # 0,0,1
        ops.append((-1*d,-1*e,-1*f,a,b,c,g,h,i))
    elif op[0]==3:
        p=op[1]
        a,b,c,d,e,f,g,h,i=ops[-1]
        # -1,0,2p
        # 0,1,0
        # 0,0,1
        ops.append((2*g*p-a,2*h*p-b,2*i*p-c,d,e,f,g,h,i))
    else:
        p=op[1]
        a,b,c,d,e,f,g,h,i=ops[-1]
        # 1,0,0
        # 0,-1,2p
        # 0,0,1
        ops.append((a,b,c,2*g*p-d,2*h*p-e,2*i*p-f,g,h,i))

Q=int(input())
for i in range(Q):
    A,B=map(int, input().split())
    X,Y=dots[B-1]
    a,b,c,d,e,f,g,h,i=ops[A]
    x=a*X+b*Y+c
    y=d*X+e*Y+f
    print("{} {}".format(x,y))
