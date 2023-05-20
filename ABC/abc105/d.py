from collections import defaultdict
N,M=map(int, input().split())
array=list(map(int, input().split()))
table=defaultdict(int)
sum=0
for a in array:
    sum+=a
    sum%=M
    table[sum]+=1
ret=0
diff=0
for a in array:
    ret+=table[diff]
    diff+=a
    diff%=M
    table[diff]-=1
print(ret)
