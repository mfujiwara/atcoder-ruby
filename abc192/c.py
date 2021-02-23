N,K=map(int, input().split())

def eval(a):
    sortedstr=sorted(list(str(a)))
    g1=int("".join(sortedstr[::-1]))
    g2=int("".join(sortedstr))
    return g1-g2
ret=N
for i in range(K):
    ret=eval(ret)
print(ret)
