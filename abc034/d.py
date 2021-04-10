N,K=map(int, input().split())
array=[]
max_i=-1
max_v=-1
for i in range(N):
    w,p=map(int, input().split())
    array.append((w,p))
    if max_v<p:
        max_v=p
        max_i=i
# (W*P+w*p)/(W+w)-P
# = (W*P-W*P-w*P+w*p)/(W+w)
# = w*(p-P)/(W+w)
done=[False]*N
done[max_i]=True
W=array[max_i][0]
S=array[max_i][0]*array[max_i][1]
max_i=-1
max_v=-1
for _ in range(K-1):
    for i in range(N):
        if done[i]: continue
        w,p=array[i]
        v=(S+w*p)/(W+w)
        if max_v<v:
            max_v=v
            max_i=i
    W+=array[max_i][0]
    S+=array[max_i][0]*array[max_i][1]
    done[max_i]=True
    max_i=-1
    max_v=-1
print(S/W)
