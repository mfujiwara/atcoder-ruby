import collections
N=int(input())
S=input()
if len(S)==2:
    if S[0]==S[1]:
        print("Yes")
    else:
        print("No")
else:
    if S[0]=="B" or S[-1]=="A":
        print("Yes")
    else:
        print("No")
