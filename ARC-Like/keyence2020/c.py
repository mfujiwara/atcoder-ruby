N,K,S=map(int, input().split())
T=S+1 if S<10**9 else S-1
print(" ".join(list(map(str, [S if i<K else T for i in range(N)]))))
