N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
evens=[]
odds=[]
for i in range(N):
    v=b_array[i]-a_array[i]
    if i%2==0:
        evens.append(v)
    else:
        odds.append(v)
evens.sort()
odds.sort()
ret=sum(a_array)
while evens and evens[-1]+odds[-1]>0:
    ret+=evens.pop()+odds.pop()
print(ret)
