import bisect
MOD=998244353
N=int(input())
S=input()
counts=[0,0,0,N]
ret=1
for i,ch in enumerate(S):
    if ch=="R":
        x=0
    elif ch=="G":
        x=1
    else:
        x=2
    sorted_count=sorted(counts)
    index=bisect.bisect_right(sorted_count,counts[x])
    #print(sorted_count[index],counts[x],sorted_count[index]-counts[x])
    # 一番多い色が出たら新しい人が選ぶ
    # そうでない場合、次に多い色を選んだ人が選ぶ
    ret*=sorted_count[index]-counts[x]
    counts[x]+=1
    ret%=MOD
print(ret)
