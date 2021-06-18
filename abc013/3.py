N,H=map(int, input().split())
A,B,C,D,E=map(int, input().split())
B+=E
D+=E
H-=E*N
H*=-1
ret=1<<60
for i in range(N+1):
    h=H-B*i
    if h<0:
        j=0
    else:
        j=h//D+1
    r=A*i+C*j
    ret=min(ret,r)
print(ret)
