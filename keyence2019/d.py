import collections
MOD=10**9+7
N,M=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
if len(a_array)!=len(set(a_array)) or len(b_array)!=len(set(b_array)):
    print(0)
    exit()
dic=collections.defaultdict(int)
for a in a_array:
    dic[a]+=1
for b in b_array:
    dic[b]+=2
keys=sorted(dic.keys())
n=N
m=M
count=0
ret=1
for v in keys:
    value=dic[v]
    if value==1:
        if count+m>v:
            print(0)
            exit()
        ret*=m
        ret%=MOD
        count+=1
        for _ in range(m-1):
            ret*=v-count
            ret%=MOD
            count+=1
        n-=1
    elif value==2:
        if count+n>v:
            print(0)
            exit()
        ret*=n
        ret%=MOD
        count+=1
        for _ in range(n-1):
            ret*=v-count
            ret%=MOD
            count+=1
        m-=1
    elif value==3:
        if count+n+m-1>v:
            print(0)
            exit()
        count+=1
        for _ in range(n+m-2):
            ret*=v-count
            ret%=MOD
            count+=1
        n-=1
        m-=1
print(ret)
