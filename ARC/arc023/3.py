MOD=pow(10,9)+7
import functools
def kaijou(a, b):
    return functools.reduce(lambda i, j: i*j%MOD, range(b,a+1), 1)
N=int(input())
count=0
array=list(map(int, input().split()))
ret=1
for i,a in enumerate(array):
    if a==-1:
        count+=1
    elif count>0:
        diff=a-array[i-count-1]
        #diff+count_C_count
        r=kaijou(diff+count,diff+1)
        r=r*pow(kaijou(count,1),MOD-2,MOD)%MOD
        ret*=r
        ret%=MOD
        count=0
print(ret)
