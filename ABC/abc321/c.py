import functools
K=int(input())
now=[0]*11
for _ in range(K):
    for i in range(10):
        if now[i]==9 or now[i]==now[i+1]-1:
            now[i]=i
        else:
            if i==0:
                now[i]+=1
            elif now[i]==0:
                now[i]=now[i-1]+1
            else:
                now[i]+=1
            break
while now[-1]==0:
    now.pop()
print("".join(map(str,now[::-1])))
