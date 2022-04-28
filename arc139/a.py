N=int(input())
array=list(map(int, input().split()))
a=0
for t in array:
    if pow(2,t)>a:
        a=pow(2,t)
    elif pow(2,t)&a==0:
        a=((a>>t)<<t)+pow(2,t)
    else:
        a=((a>>t)<<t)+pow(2,t+1)
print(a)
