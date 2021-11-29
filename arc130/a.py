N=int(input())
S=input()+"_"
ret=0
count=1
for i in range(1,N+1):
    if S[i]==S[i-1]:
        count+=1
    else:
        ret+=count*(count-1)//2
        count=1
print(ret)
