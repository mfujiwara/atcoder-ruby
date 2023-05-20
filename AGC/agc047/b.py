N=int(input())
root=[{},[0]*26]
ret=0
sss=[]
for _ in range(N):
    sss.append(input())
sss.sort(key=lambda e: -len(e))
for s in sss:
    s=list(map(lambda e: ord(e)-ord("a"),list(s)))
    node=root
    nodes=[root]
    for i in range(len(s)-1,0,-1):
        k=s[i]
        if k not in node[0]:
            node[0][k]=[{},[0]*26]
        node=node[0][k]
        nodes.append(node)
    ret+=node[1][s[0]]
    heads=set()
    heads.add(s[0])
    nodes.pop()
    for i in range(1,len(s)):
        heads.add(s[i])
        node=nodes.pop()
        for j in range(26):
            if j in heads:
                node[1][j]+=1
print(ret)
