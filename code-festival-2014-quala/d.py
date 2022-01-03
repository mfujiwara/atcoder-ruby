A,K=map(int, input().split())
B=str(A)
ret=10**15
for i in range(len(B)):
    for j in range(10):
        for k in range(10):
            v=int(B[:i]+str(j)+str(k)*(len(B)-1-i))
            if len(set(list(str(v))))<=K:
                ret=min(ret,abs(v-A))
print(ret)
