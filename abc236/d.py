N=int(input())
A=[]
for i in range(2*N-1):
    A.append(list(map(int, input().split())))
def calc(array,perm):
    if len(array)==0:
        v=0
        for i in range(N):
            a,b=perm[i*2],perm[i*2+1]
            if a>b:
                a,b=b,a
            v^=A[a][b-a-1]
        return v
    else:
        ret=0
        for i in range(1,len(array)):
            perm.append(array[0])
            perm.append(array[i])
            arr=array[:]
            del arr[i]
            del arr[0]
            ret=max(ret,calc(arr,perm))
            perm.pop()
            perm.pop()
        return ret
print(calc([i for i in range(2*N)],[]))
