T=int(input())
for _ in range(T):
    N=int(input())
    array=list(map(int, input().split()))
    S=list(map(int, list(input())))

    memo=[]
    b=True
    for i in range(N-1,-1,-1):
        a=array[i]
        for m in memo:
            a=min(a,a^m)
        if S[i]==0:
            if a!=0:
                memo.append(a)
        else:
            if a!=0:
                b=False
                break
    if b:
        print(0)
    else:
        print(1)
