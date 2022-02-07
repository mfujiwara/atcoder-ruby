T=int(input())
for _ in range(T):
    a,s=map(int, input().split())
    diff=s-a*2
    if diff>=0 and diff&a==0:
        print("Yes")
    else:
        print("No")
