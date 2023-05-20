N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
memo={}
for i,a in enumerate(a_array):
    memo[a]=i
ret1=0
ret2=0
for i,b in enumerate(b_array):
    if b in memo:
        if memo[b]==i:
            ret1+=1
        else:
            ret2+=1
print(ret1)
print(ret2)
