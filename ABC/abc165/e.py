N,M=map(int, input().split())
rets=[]
m1=(M+1)//2
m2=M//2
for i in range(m1):
    # m1-1 -> m1+1
    # 0 -> 
    rets.append((i+1,2*m1-i))
for i in range(m2):
    rets.append((i+1+2*m1,2*m2+1-i+2*m1))
for a,b in rets:
    print(f"{a} {b}")
