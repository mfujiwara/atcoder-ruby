N=int(input())
S=input()
r_count=0
g_count=0
b_count=0
for ch in S:
    if ch=="R":
        r_count+=1
    elif ch=="G":
        g_count+=1
    else:
        b_count+=1
ret=r_count*g_count*b_count
d=1
while d*2<N:
    for i in range(N-2*d):
        if S[i]!=S[i+d] and S[i]!=S[i+2*d] and S[i+d]!=S[i+2*d]:
            ret-=1
    d+=1
print(ret)
