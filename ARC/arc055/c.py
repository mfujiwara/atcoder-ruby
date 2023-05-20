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
L=len(S)
#print(L)
zzz=z_algorithm(S)
zzzr=z_algorithm(S[::-1])[::-1]
ret=0
for i in range(3,len(S)-1):
    v=min(zzz[i],i-2,L-1-i) # あり得るAの長さ
    vr=min(zzzr[i-1],L-1-i,i-2) # あり得るCの長さ
    if v>0 and vr>0 and i+v+vr+1>=L and i*2>L:
        ret+=i+v+vr+1-L
        #print(i,v,vr,i+v+vr+1-L)
print(ret)
