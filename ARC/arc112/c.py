import collections
N=int(input())
array=list(map(lambda e: int(e)-1, input().split()))
children=collections.defaultdict(list)
for i,a in enumerate(array):
    children[a].append(i+1)
memo=[-1]*N # (手番がそのまま,先手の得る数,後手の得る数)
targets=[0]
while targets:
    t=targets.pop()
    if len(children[t])==0:
        memo[t]=(False,1,0) #葉の評価
    elif memo[children[t][0]]==-1:
        targets.append(t)
        for u in children[t]:
            targets.append(u)
    else:
        black=1
        white=0
        turn=False
        group1=[] #手番変わる
        group2=[] #手番変わらない取りたくない
        for u in children[t]:
            b,n1,n2=memo[u]
            if b:
                if n1<=n2:
                    white+=n2
                    black+=n1
                else:
                    group2.append((n1-n2,n2,n1))
            else:
                group1.append((n1-n2,n2,n1))
        group1.sort()
        for _,n2,n1 in group1:
            if turn:
                black+=n2
                white+=n1
            else:
                white+=n2
                black+=n1
            turn=not turn
        for _,n2,n1 in group2:
            if turn:
                black+=n2
                white+=n1
            else:
                white+=n2
                black+=n1
        memo[t]=(turn,black,white)
print(memo[0][1])
