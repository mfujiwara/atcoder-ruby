import sys
H,W,N=map(int, input().split())
s_r,s_c=map(int, input().split())
S=input()
T=input()
L=s_c
R=s_c
U=s_r
D=s_r
for i in range(N):
    if S[i]=="L":
        L-=1
    elif S[i]=="R":
        R+=1
    elif S[i]=="U":
        U-=1
    else:
        D+=1
    if L==0 or R==W+1 or U==0 or D==H+1:
        print("NO")
        sys.exit()
    if T[i]=="R" and L<W:
        L+=1
    elif T[i]=="L" and R>1:
        R-=1
    elif T[i]=="D" and U<H:
        U+=1
    elif T[i]=="U" and D>1:
        D-=1
print("YES")
