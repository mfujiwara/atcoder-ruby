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
len_s=len(S)
len_t=len(T)
n=len_t//len_s+2
SS=S*n
zzz=z_algorithm(T+SS)[len_t:]
indexs=[]
for i in range(len_s):
    if zzz[i]>=len_t:
        indexs.append(i)
index_set=set(indexs)
# print(SS)
# print(zzz)
# print(indexs)
done=set()
ret=0
for i in indexs:
    if i in done:
        continue
    done.add(i)
    c=1
    # プラス方向を調べる
    k=(i+len_t)%len_s
    while k in index_set:
        if k in done:
            print(-1)
            exit()
        done.add(k)
        k=(k+len_t)%len_s
        c+=1
    # マイナス方向を調べる
    k=(i-len_t)%len_s
    while k in index_set:
        if k in done:
            print(-1)
            exit()
        done.add(k)
        k=(k-len_t)%len_s
        c+=1
    ret=max(ret,c)
print(ret)
