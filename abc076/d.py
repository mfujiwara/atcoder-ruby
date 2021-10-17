N=int(input())
t_array=list(map(int, input().split()))
v_array=list(map(int, input().split()))
for i in range(N):
    v_array[i]*=2
    t_array[i]*=2
points=[0]
for i in range(N):
    pv=points[-1]
    t=t_array[i]
    v=v_array[i]
    if pv>=v:
        for _ in range(t):
            points.append(v)
    elif t>v-pv:
        for j in range((v-pv)): 
            points.append(pv+(j+1))
        for j in range((t-v+pv)):
            points.append(v)
    else:
        for j in range(t):
            points.append(pv+(j+1))
points_r=[0]
for i in range(N-1,-1,-1):
    pv=points_r[-1]
    t=t_array[i]
    v=v_array[i]
    if pv>=v:
        for _ in range(t):
            points_r.append(v)
    elif t>v-pv:
        for j in range((v-pv)): 
            points_r.append(pv+(j+1))
        for j in range((t-v+pv)):
            points_r.append(v)
    else:
        for j in range(t):
            points_r.append(pv+(j+1))
points_r=points_r[::-1]
ret=0
for i in range(len(points)):
    s=min(points[i],points_r[i])
    ret+=s
print(ret/4)
