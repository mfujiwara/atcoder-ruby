N=int(input())
done=set()
done.add((1,2,3,4,5,6))
memo=[(1,2,3,4,5,6)]
for i in range(N):
    k=i%5
    nexts=list(memo[-1])
    nexts[k],nexts[k+1]=nexts[k+1],nexts[k]
    nexts=tuple(nexts)
    if nexts in done:
        break
    else:
        done.add(nexts)
        memo.append(nexts)
print("".join(list(map(str,list(memo[N%len(memo)])))))
