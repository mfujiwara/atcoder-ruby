MOD=998244353
inv2=MOD-(MOD//2)
N,M=map(int, input().split())
Q=int(input())
rets=[]
for _ in range(Q):
    a,b,c,d=map(int, input().split())
    def calc(a,b,c,d):
        # a,c
        if (a+c)%2==1:
            c+=1
        ac=(a-1)*M%MOD+c
        ac%=MOD
        # a,d
        if (a+d)%2==1:
            d-=1
        ad=(a-1)*M%MOD+d
        ad%=MOD
        #print("ac,ad",ac,ad,a,b,c,d)
        if c<=d:
            col_count=(ad-ac+2)*inv2%MOD
            first_row=(ac+ad)*col_count*inv2%MOD
        else:
            col_count=0
            first_row=0
        row_count=(b-a+2)//2
        return row_count*(2*first_row%MOD+(row_count-1)*col_count%MOD*M%MOD*2%MOD)%MOD*inv2%MOD
    ret1=calc(a,b,c,d)
    ret2=calc(a+1,b,c,d)
    print((ret1+ret2)%MOD)
#print(rets)
