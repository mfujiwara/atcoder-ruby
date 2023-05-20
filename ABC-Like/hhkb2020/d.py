MOD=pow(10,9)+7
T=int(input())
for _ in range(T):
    N,A,B=map(int, input().split())
    if N<A+B:
        print(0)
        continue
    w=(N-A+1)*(N-B+1)%MOD
    x=(N-A-B+2)*(N-A-B+1)%MOD
    y=(w-x+MOD)%MOD
    z=pow(y,2,MOD)
    ret=(pow(w,2,MOD)-z+MOD)%MOD
    print(ret)
