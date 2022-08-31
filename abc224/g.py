N,S,T,A,B=map(int, input().split())
ok=T
ng=0
while ng+1<ok:
    mid=(ok+ng)//2
    # +1した場合
    c0=(T-mid)*A
    # ランダムにした場合
    # c1=c1*(N-T+mid)/N+(T-mid-1)*A*(T-mid)/2/N+B
    # (T-mid/N)*c1=(T-mid-1)*A*(T-mid)/2/N+B
    # (T-mid)*c1=(T-mid-1)*A*(T-mid)/2+B*N
    c1=((T-mid-1)*A*(T-mid)/2+B*N)/(T-mid)
    if c0<c1:
        ok=mid
    else:
        ng=mid
if ok<=S<=T:
    print((T-S)*A)
else:
    v=((T-ng-1)*A*(T-ng)/2+B*N)/(T-ng)
    if v>pow(10,9):
        print(int(v))
    else:
        print(v)
