def det_is_even(A):
    size=len(A)
    for i in range(size):
        for j in range(i+1,size):
            if A[i][i]==0 and A[j][i]==0:
                continue
            elif A[i][i]==0 and A[j][i]!=0:
                for k in range(size):#行の交換
                    A[i][k],A[j][k]=A[j][k],A[i][k]
            A[j]=[(A[i][k]*A[j][i]-A[j][k]*A[i][i])%2 for k in range(size)] #A[i]*A[j][i]-A[j]*A[i][i]
    for i in range(size):
        if A[i][i]%2==0:
            return True
    return False
N=int(input())
S=[list(map(int, list(input()))) for _ in range(N)]
is_event=det_is_even(S)
if is_event:
    print("Even")
else:
    print("Odd")
