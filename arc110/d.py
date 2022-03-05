import functools
MOD=pow(10,9)+7
def kaijou(a, b):
    return functools.reduce(lambda i, j: i*j%MOD, range(b,a+1), 1)
N,M=map(int, input().split())
array=list(map(int, input().split()))
total=sum(array)
ret=kaijou(M+N,M-total+1)*pow(kaijou(total+N,1),MOD-2,MOD)%MOD
print(ret)
