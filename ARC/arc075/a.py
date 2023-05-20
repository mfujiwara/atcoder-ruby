N=int(input())
mini=101
total=0
for _ in range(N):
    s=int(input())
    total+=s
    if s%10!=0:
        mini=min(mini,s)
#print(total,min5)
if total%10!=0:
    print(total)
elif mini==101:
    print(0)
else:
    print(total-mini)
