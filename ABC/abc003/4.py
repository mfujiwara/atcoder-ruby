import functools
MOD=pow(10,9)+7
def kaijou(a, b):
    return functools.reduce(lambda i, j: i*j%MOD, range(b,a+1), 1)
R,C=map(int, input().split())
X,Y=map(int, input().split())
D,L=map(int, input().split())
@functools.lru_cache(maxsize=None)
def comb(x,y):
    xy=x*y
    if x<=0 or y<=0 or xy<D+L:
        return 0
    ret=1
    # x*yからD
    ret*=kaijou(xy,xy-D+1)
    ret%=MOD
    ret*=pow(kaijou(D,1),MOD-2,MOD)
    ret%=MOD
    # x*y-DからL
    ret*=kaijou(xy-D,xy-D-L+1)
    ret%=MOD
    ret*=pow(kaijou(L,1),MOD-2,MOD)
    ret%=MOD
    #print(x,y,ret)
    return ret
# 0_1
ret=comb(X,Y)
# 1_4
ret-=comb(X-1,Y)*2
ret+=2*MOD
ret%=MOD
ret-=comb(X,Y-1)*2
ret+=2*MOD
ret%=MOD
# 2_6
ret+=comb(X-2,Y)
ret%=MOD
ret+=comb(X,Y-2)
ret%=MOD
ret+=comb(X-1,Y-1)*4
ret%=MOD
# 3_4
ret-=comb(X-2,Y-1)*2
ret+=2*MOD
ret%=MOD
ret-=comb(X-1,Y-2)*2
ret+=2*MOD
ret%=MOD
# 4_1
ret+=comb(X-2,Y-2)
ret%=MOD
ret= ret*(R-X+1)*(C-Y+1)%MOD
print(ret)
