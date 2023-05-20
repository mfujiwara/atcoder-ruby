import sys
A,B,C=map(int, input().split())
A%=10
array=[]
if A==0:
    array= [0]
elif A==1:
    array= [1]
elif A==2:
    array= [2,4,8,6]
elif A==3:
    array= [3,9,7,1]
elif A==4:
    array= [4,6]
elif A==5:
    array= [5]
elif A==6:
    array= [6]
elif A==7:
    array= [7,9,3,1]
elif A==8:
    array= [8,4,2,6]
else:
    array= [9,1]
if len(array)==1:
    print(array[0])
    sys.exit()
if len(array)==2:
    if B%2==0:
        print(array[1])
    else:
        print(array[0])
    sys.exit()
B%=4
MOD=4
def ppow(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return ppow(x**2 % MOD, n // 2)
    elif (n % 2) == 1:
        return ppow(x**2 % MOD, n // 2) * x
r=ppow(B,C)
if r==0:
    print(array[3])
elif r==1:
    print(array[0])
elif r==2:
    print(array[1])
else:
    print(array[2])
