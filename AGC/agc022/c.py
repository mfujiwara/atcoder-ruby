N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
if a_array==b_array:
    print(0)
    exit()
for i in range(N):
    a=a_array[i]
    b=b_array[i]
    if a!=b and b*2>=a:
        print(-1)
        exit()
rets=[]
def calc(kouho):
    node_size=51
    d=[[1]*node_size for _ in range(node_size)]
    for k in kouho:
        for n in range(0,51):
            d[n][n%k]=0
    for k in rets:
        for n in range(0,51):
            d[n][n%k]=0
    for k in range(node_size):
        for i in range(node_size):
            for j in range(node_size):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    for i in range(N):
        if d[a_array[i]][b_array[i]]>0:
            return False
    return True
kouho=[i for i in range(1,51)]
ret=0
while kouho:
    v=kouho.pop()
    if not calc(kouho):
        rets.append(v)
        ret+=1<<v
print(ret)
