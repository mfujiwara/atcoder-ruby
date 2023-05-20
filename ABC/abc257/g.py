import bisect
def z_algorithm(s):
    N = len(s)
    Z_alg = [0]*N

    Z_alg[0] = N
    i = 1
    j = 0
    while i < N:
        while i+j < N and s[j] == s[i+j]:
            j += 1
        Z_alg[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + Z_alg[k]<j:
            Z_alg[i+k] = Z_alg[k]
            k += 1
        i += k
        j -= k
    return Z_alg
S=input()
T=input()
z=z_algorithm(S+T)[len(S):]
#print(z)
# dp[i]:=i個連結してできるTの接頭辞の最大長
ret=0
# あるステップで開始位置にできる範囲
ranges=[0,1]
while ranges[0]<ranges[1] and ranges[1]<=len(T):
    nexts=[ranges[1],ranges[1]]
    for i in range(ranges[0],ranges[1]):
        c=min(z[i],len(S))
        nexts[1]=max(nexts[1],i+c+1)
    ranges=nexts
    ret+=1
    #print(ranges)
if ranges[1]>len(T):
    print(ret)
else:
    print(-1)
