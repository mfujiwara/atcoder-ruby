N=int(input())
ret=0
for i in range(16):
    base=pow(10,i)
    v=base
    for j in range(1,17):
        if v>N:
            break
        if i==0:
            if v<=N:
                ret+=j
        else:
            if v+base-1<=N:
                ret+=(base-base//10)*j
            elif v+base//5<=N:
                ret+=(base-base//10-(v+base-1-N))*j
            elif v+base//10<=N:
                ret+=base//10*j
            else:
                ret+=(N-v+1)*j
        v=v*10+base
print(ret)
