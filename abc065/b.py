N=int(input())
dic={}

for i in range(N):
    a=int(input())
    dic[i+1]=a
done=set()
a=1
done.add(1)
ret=0
while True:
    ret+=1
    next=dic[a]
    if next==2:
        print(ret)
        exit()
    if next in done:
        break
    a=next
    done.add(next)
print(-1)
