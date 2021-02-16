B,C=map(int, input().split())
if B>0:
    zero=1 if B*2<=C else 0
    minus_more=(C-1)//2
    plus_more=max((C-2)//2,0)
    minus_less=min(B,(C+1)//2)
    plus_less=min(B,(C+2)//2)
    print(zero+minus_more+plus_more+minus_less+plus_less)
elif B==0:
    zero=1
    minus_more=C//2
    plus_more=(C-1)//2
    minus_less=0
    plus_less=0
    print(zero+minus_more+plus_more+minus_less+plus_less)
else:
    zero=1 if 0<=C-1+B*2 else 0
    minus_more=C//2
    plus_more=(C-1)//2
    minus_less=min(abs(B),(C-2)//2)
    plus_less=min(abs(B),(C-1)//2)
    print(zero+minus_more+plus_more+minus_less+plus_less)
