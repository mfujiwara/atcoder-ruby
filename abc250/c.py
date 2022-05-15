N,Q=map(int, input().split())
index=[i for i in range(N)]
balls=[i+1 for i in range(N)]
for _ in range(Q):
    #print(*balls)
    x=int(input())
    x_index=index[x-1]
    if x_index+1<N:
        y=balls[x_index+1]
    else:
        y=balls[x_index-1]
    y_index=index[y-1]
    balls[x_index],balls[y_index]=balls[y_index],balls[x_index]
    index[x-1],index[y-1]=index[y-1],index[x-1]
print(*balls)
