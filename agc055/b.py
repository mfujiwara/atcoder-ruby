N=int(input())
S=input()
T=input()
ord_A=ord("A")
sss=[]
for i,ch in enumerate(S):
    v=((ord(ch)-ord_A-i)%3+3)%3
    if len(sss)>=2 and sss[-1]==v and sss[-2]==v:
        sss.pop()
        sss.pop()
    else:
        sss.append(v)
ttt=[]
for i,ch in enumerate(T):
    v=((ord(ch)-ord_A-i)%3+3)%3
    if len(ttt)>=2 and ttt[-1]==v and ttt[-2]==v:
        ttt.pop()
        ttt.pop()
    else:
        ttt.append(v)
if sss==ttt:
    print("YES")
else:
    print("NO")
