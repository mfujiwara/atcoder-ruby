N=int(input())
targets=[N]
memo={}
memo[0]=1
while targets:
    t=targets.pop()
    if t in memo:
        continue
    if t//2 in memo and t//3 in memo:
        memo[t]=memo[t//2]+memo[t//3]
    else:
        targets.append(t)
        if t//2 not in memo:
            targets.append(t//2)
        if t//3 not in memo:
            targets.append(t//3)
print(memo[N])
