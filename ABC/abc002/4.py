import sys
N,M=map(int, input().split())
if M*2==N*(N-1):
    print(N)
    sys.exit()

rels=[[False]*N for _ in range(N)]
for i in range(M):
    x,y=map(int, input().split())
    rels[x-1][y-1]=True
    rels[y-1][x-1]=True

def calc(men, next_index):
    if next_index==N:
        return len(men)
    judge=True
    for man in men:
        if not rels[man][next_index]:
            judge=False
            break
    if judge:
        return max(
            calc(men[:]+[next_index],next_index+1),
            calc(men,next_index+1)
        )
    else:
        return calc(men,next_index+1)
ret=calc([],0)
print(ret)
