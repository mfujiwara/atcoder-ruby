A,B,K,L=map(int, input().split())
r1=K*A
r2=(K+L-1)//L*B
c=K//L
r3=c*B+A*(K-c*L)
print(min(r1,r2,r3))
