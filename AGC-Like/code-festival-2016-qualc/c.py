MOD=10**9+7
N=int(input())
t_array=list(map(int, input().split()))
a_array=list(map(int, input().split()))[::-1]
t_minmax=[]
before_max=0
for t in t_array:
    if t>before_max:
        t_minmax.append((t,t))
        before_max=t
    else:
        t_minmax.append((1,before_max))
a_minmax=[]
before_max=0
for a in a_array:
    if a>before_max:
        a_minmax.append((a,a))
        before_max=a
    else:
        a_minmax.append((1,before_max))
a_minmax=a_minmax[::-1]
r=1
for i in range(N):
    t_min,t_max=t_minmax[i]
    a_min,a_max=a_minmax[i]
    min_val=max(t_min,a_min)
    max_val=min(t_max,a_max)
    num=max(0,max_val-min_val+1)
    r*=num
    r%=MOD
print(r)
