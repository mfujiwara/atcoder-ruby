N,M=map(int, input().split())
S=[]
for bit in range(N):
    # 3進数で1の位が0、他の桁も1,0のみが現れる数を小さいものからN個構成する
    v=0
    tmp=3
    while bit:
        bit,r=divmod(bit,2)
        if r==1:
            v+=tmp
        tmp*=3
    S.append(v)
#print(S)
# Sの合計とMとの差分がNで割れるように調整する
X=(M-sum(S))%N
for i in range(X):
    S[i] += 1
diff=(sum(S)-M)//N
print(*[s - diff for s in S])
