A,K=map(int, input().split())
if K==0:
    print(2*10**12-A)
    exit()
a=A
t=0
while a<2*10**12:
    a+=a*K+1
    t+=1
print(t)
