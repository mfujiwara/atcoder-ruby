N=int(input())
if N==3 or N==5 or N==2:
    print("Prime")
    exit()
if N%2==0 or N%5==0 or N==1:
    print("Not Prime")
    exit()
t=0
while N>0:
    N,r=divmod(N,10)
    t+=r
if t%3==0:
    print("Not Prime")
    exit()
print("Prime")
