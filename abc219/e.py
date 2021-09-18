towns=[]
for i in range(4):
    for j,a in enumerate(list(map(int, input().split()))):
        if a==1:
            towns.append((i,j))
ret=0
for bit in range(1,pow(2,16)):
    blocks=[]
    not_blocks=[(-1,-1),(-1,0),(-1,1),(-1,2),(-1,3),(-1,4),(0,-1),(0,4),(1,-1),(1,4),(2,-1),(2,4),(3,-1),(3,4),(4,-1),(4,0),(4,1),(4,2),(4,3),(4,4)]
    for k in range(16):
        bit,r=divmod(bit,2)
        i,j=divmod(k,4)
        if r==1:
            blocks.append((i,j))
        else:
            not_blocks.append((i,j))        
    valid=True
    for town in towns:
        if town not in blocks:
            valid=False
            break
    if not valid:
        continue

    targets=[blocks.pop()]
    while targets:
        r,c=targets.pop()
        if (r-1,c) in blocks:
            blocks.remove((r-1,c))
            targets.append((r-1,c))
        if (r+1,c) in blocks:
            blocks.remove((r+1,c))
            targets.append((r+1,c))
        if (r,c-1) in blocks:
            blocks.remove((r,c-1))
            targets.append((r,c-1))
        if (r,c+1) in blocks:
            blocks.remove((r,c+1))
            targets.append((r,c+1))
    if len(blocks)!=0:
        continue

    targets=[not_blocks.pop()]
    while targets:
        r,c=targets.pop()
        if (r-1,c) in not_blocks:
            not_blocks.remove((r-1,c))
            targets.append((r-1,c))
        if (r+1,c) in not_blocks:
            not_blocks.remove((r+1,c))
            targets.append((r+1,c))
        if (r,c-1) in not_blocks:
            not_blocks.remove((r,c-1))
            targets.append((r,c-1))
        if (r,c+1) in not_blocks:
            not_blocks.remove((r,c+1))
            targets.append((r,c+1))

    if len(not_blocks)!=0:
        continue
    ret+=1
print(ret)
