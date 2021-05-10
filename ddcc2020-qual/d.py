M=int(input())
count=0
sum=0
for _ in range(M):
    d,c=map(int, input().split())
    count+=c
    sum+=d*c
print(count-1+(sum-1)//9)
