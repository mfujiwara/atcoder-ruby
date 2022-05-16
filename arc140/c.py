N,X=map(int, input().split())
back1=[N+1,0]
back2=[0,N+1]
done=set()
while abs(back1[-1]-back1[-2])>1:
    diff=back1[-2]-back1[-1]
    if diff>0:
        next=back1[-1]+diff-1
        if next==X and len(done)!=N-1:
            next-=1
    else:
        next=back1[-1]+diff+1
        if next==X and len(done)!=N-1:
            next+=1
    if next in done:
        break
    back1.append(next)
    done.add(next)
done=set()
while abs(back2[-1]-back2[-2])>1:
    diff=back2[-2]-back2[-1]
    if diff>0:
        next=back2[-1]+diff-1
        if next==X and len(done)!=N-1:
            next-=1
    else:
        next=back2[-1]+diff+1
        if next==X and len(done)!=N-1:
            next+=1
    if next in done:
        break
    back2.append(next)
    done.add(next)
#print(back1)
#print(back2)
if len(back1)>=len(back2):
    back=back1
else:
    back=back2
back=back[2:][::-1]
if back[0]==X:
    print(*back)
else:
    rets=[X]
    for i in range(1,N+1):
        if i not in done and i!=X:
            rets.append(i)
    print(*(rets+back))
