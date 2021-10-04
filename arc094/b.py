Q=int(input())
for _ in range(Q):
    a,b=map(int, input().split())
    v=a*b
    if a==b:
        r=(v-1)//(a+1)*2
        print(r)
        continue
    if a>b:
        a,b=b,a
    r=(v-1)//(b+1)
    c=int(pow(v,0.5))
    if c*c==v:
        d=c-1
    elif c*(c+1)<v:
        d=c+1
    else:
        d=c
    r+=d+c-a-1
    print(r)
