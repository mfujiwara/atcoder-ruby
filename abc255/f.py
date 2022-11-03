N=int(input())
p_array=list(map(int, input().split()))
q_array=list(map(int, input().split()))
if p_array[0]!=1:
    print(-1)
    exit()
q_index={}
for i,q in enumerate(q_array):
    q_index[q]=i
targets=[(0,N,0,N)]
rets=[[0,0] for _ in range(N)]
while targets:
    s0,t0,s1,t1=targets.pop()
    index=q_index[p_array[s0]]
    if s1<=index<t1:
        if s1!=index:
            d=index-s1
            targets.append((s0+1,s0+1+d,s1,s1+d))
            rets[p_array[s0]-1][0]=p_array[s0+1]
        if index!=t1-1:
            d=t1-index-1
            targets.append((t0-d,t0,index+1,index+1+d))
            rets[p_array[s0]-1][1]=p_array[t0-d]
    else:
        print(-1)
        exit()
for ret in rets:
    print(*ret)
