N,K=map(int, input().split())
array=list(range(1,N+1))
b=N
for i in range(N-1,-1,-1):
    ret=(b+K-1)//K-1 # i+1個のグループのうち何番目か
    print(array.pop(ret))
    b=(b-K*ret)*i # ret番目のグループを拡大してi個のグループとして考える
