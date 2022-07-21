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
N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
diff_baa=[]
for i in range(N):
    diff_baa.append(b_array[i]^b_array[(i+1)%N])
for i in range(N*2):
    diff_baa.append(a_array[i%N]^a_array[(i+1)%N])
z_array=z_algorithm(diff_baa)
k_array=[]
for i in range(N,2*N):
    if z_array[i]>=N:
        k_array.append(i-N)
for k in k_array:
    x=b_array[0]^a_array[k]
    print(k,x)
