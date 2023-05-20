N=int(input())
A=input()
zero_one=0
for i,a in enumerate(A):
    a=int(a)-1
    if ((N-1)^i)&i==0 and a==1:
        zero_one+=1
        zero_one%=2
if zero_one==1:
    print(1)
    exit()
elif "2" in A:
    print(0)
    exit()
zero_one=0
for i,a in enumerate(A):
    a=(int(a)-1)//2
    if ((N-1)^i)&i==0:
        zero_one^=a
if zero_one==1:
    print(2)
else:
    print(0)
