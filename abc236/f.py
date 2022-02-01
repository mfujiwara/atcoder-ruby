N=int(input())
array=list(map(int, input().split()))
array=sorted([(c,i+1) for i,c in enumerate(array)],reverse=True)
done=set([0])
ret=0
while len(done)<pow(2,N):
    c,i=array.pop()
    if i not in done:
        ret+=c
        tmp=set()
        for d in done:
            tmp.add(d^i)
        done|=tmp
print(ret)
