N=int(input())
mini=0
ret=0
for _ in range(N):
    a=int(input())
    if a<=mini:
        continue
    if a==mini+1:
        mini+=1
        continue
    ret+=(a-1)//(mini+1)
    mini=max(mini,1)
print(ret)
