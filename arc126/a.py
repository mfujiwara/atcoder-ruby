T=int(input())
def calc(a,b,c):
    ret=0
    # 6,4
    x=min(b,c)
    b-=x
    c-=x
    ret+=x
    # 6,2,2
    x=min(b,a//2)
    b-=x
    a-=x*2
    ret+=x
    # 4,4,2
    x=min(c//2,a)
    c-=x*2
    a-=x
    ret+=x
    # 4,2,2,2
    x=min(c,a//3)
    c-=x
    a-=x*3
    ret+=x
    # 2,2,2,2,2
    ret+=a//5
    return ret
    
for _ in range(T):
    A,B,C=map(int, input().split())
    B//=2 #6
    v=calc(A,B,C)
    print(v)
