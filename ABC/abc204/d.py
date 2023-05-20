N=int(input())
array=list(map(int, input().split()))
total=sum(array)
dp=[False]*100001
dp[0]=True
ret=total
half=total//2
for t in array:
    for i in range(len(dp))[::-1]:
        if dp[i] and i+t<len(dp):
            dp[i+t]=True
            ret=min(ret,max(i+t,abs(total-i-t)))
print(ret)
