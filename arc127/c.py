N=int(input())
X=list(map(int, list(input())))
top=0
def minus():
    index=len(X)-1
    while X[index]==0:
        X[index]=1
        index-=1
    X[index]=0
minus()
while top<len(X) and X[top]==0:
    top+=1
print(1,end="")
while top<len(X):
    if len(X)-top<N:
        print(0,end="")
        minus()
    else:
        print(1,end="")
        X[top]=0
        top+=1
    while top<len(X) and X[top]==0:
        top+=1
    N-=1
print()
