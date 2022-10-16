def prime_factor(val):
    p=[0]*0
    for i in range(2,167167):
        if i*i>val:
            break
        if val%i==0:
            p.append(i)
            while val%i==0:
                val//=i
    if val!=1:
        p.append(val)
    return p
N=int(input())
array=list(map(int, input().split()))
array.sort()
done=set()
for i in range(N):
    a=array[i]
    b=array[(i+1)%N]
    d=abs(a-b)
    for p in prime_factor(d):
        if p==2:
            if d%4==0:
                p=4
            else:
                continue
        if p in done:
            continue
        m=array[i]%p
        count=0
        for a in array:
            if a%p==m:
                count+=2
        if count>N:
            print(p)
            exit()
        done.add(p)
print(-1)
