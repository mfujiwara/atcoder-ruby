import sys
N,K=map(int, input().split())
diff=(N-1)*(N-2)//2-K
if diff<0:
    print("-1")
    sys.exit()
m=N-1+diff
print(m)
for i in range(2,N+1):
    print("{} {}".format(1,i))
if diff==0: sys.exit()
for i in range(2,N):
    for j in range(i+1,N+1):
        print("{} {}".format(i,j))
        diff-=1
        if diff==0: sys.exit()
