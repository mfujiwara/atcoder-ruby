N,Q=map(int, input().split())
array=list(map(int, input().split()))
edges=[[] for _ in range(N)]
for i,a in enumerate(array):
    edges[a-1].append(i+1)
# print(edges)
# print(a_to_index)
for _ in range(Q):
    query=list(map(int, input().split()))
    m=query[0]
    v_set=set(query[1:])
    ret=0
    #print(ivs)
    for i in range(m):
        v=query[i+1]-1
        if v!=0 and array[v-1] in v_set:
            ret+=len(edges[v])-1
        else:
            ret+=len(edges[v])+1
        #print(v,ret,done,array)
    print(ret)
