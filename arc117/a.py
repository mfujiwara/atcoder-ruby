A,B=map(int, input().split())
a=[i+1 for i in range(A)]
b=[-i-1 for i in range(B)]
if A>B:
    v=sum(a)+sum(b)
    b[-1]-=v
elif A<B:
    v=sum(a)+sum(b)
    a[-1]-=v
print(" ".join(map(str,a+b)))
