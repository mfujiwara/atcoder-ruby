import statistics
N=int(input())
xxx=[]
yyy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xxx.append(x)
    yyy.append(y)
X=int(statistics.median(xxx))
Y=int(statistics.median(yyy))
ret=0
for x in xxx:
    ret+=abs(x-X)
for y in yyy:
    ret+=abs(y-Y)
print(ret)
