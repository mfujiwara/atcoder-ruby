N=int(input())
# array[i]:=辞書順 i 番目の文字列が始まるindex+1
array=list(map(int, input().split()))
indexes=[-1]*(N+1)
# indexes[i]:=index i から始まる文字列の辞書順
for i in range(N):
  indexes[array[i]-1]=i
#print(indexes)
rets=[-1]*N
d=0
k=-1
maxi=0
for i in range(N):
    # suffix array の順番に貪欲に埋めていく
    if indexes[array[i]]<k:
        # 次の文字が小さくなってしまう場合に、対象の文字を大きくする
        d+=1
    rets[array[i]-1]=d
    #print(rets,k)
    k=indexes[array[i]]
    maxi=max(maxi,d)
if maxi>=26:
    print(-1)
else:
    print(*[chr(r+65) for r in rets],sep="")
