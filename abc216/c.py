N=int(input())
rets=[]
while N>0:
    if N%2==0:
        N=N//2
        rets.append("B")        
    else:
        N-=1
        rets.append("A")
print("".join(rets[::-1]))
