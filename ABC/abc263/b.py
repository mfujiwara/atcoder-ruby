N=int(input())
array=list(map(int, input().split()))
dic={}
for i,a in enumerate(array):
    dic[i+2]=a
k=0
now=N
while now!=1:
    now=dic[now]
    k+=1
print(k)
