N=int(input())
S=input()
ddd=-1
T=""
for i,ch in enumerate(S):
    if i==ddd+1 and ch=="d":
        ddd+=1
    if ch=="p":
        T="d"+T
    else:
        T="p"+T
# print(T)
ret=S
prefix=S[:ddd+1]
for i in range(ddd+1,N):
    s=ddd+1
    t=i+1
    U=prefix+T[N-t:N-s]+S[i+1:]
    # print(s,t)
    # print(prefix,T[N-t:N-s],S[i+1:])
    ret=min(ret,U)
print(ret)
