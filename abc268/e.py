N=int(input())
array=list(map(int, input().split()))
point=0
# acc[i]:=iからjになる時の差分
acc=[0]*N
for i,a in enumerate(array):
    #print(acc)
    # 料理に対する不満度が0になるタイミング
    # (i+t)%N==a
    t=(a-i)%N
    acc[t]+=2
    if N%2==0:
        acc[(t+N//2)%N]-=2
    else:
        acc[(t+N//2)%N]-=1
        acc[(t+N//2+1)%N]-=1
    # 今のポイント
    now=min((a-i)%N,(i-a)%N)
    pre=min((a-i+1)%N,(i-1-a)%N)
    point+=now
    acc[0]+=now-pre
ret=point
d=0
#print(point,acc)
for a in acc:
    d+=a
    point+=d
    ret=min(ret,point)
print(ret)
