N=int(input())
S=input()
valid=True
if S[0]=="a" and len(S)%6==3:
    check="abc"
    for i,ch in enumerate(S):
        if ch!=check[i%3]:
            valid=False
            break
elif S[0]=="b" and len(S)%6==1:
    check="bca"
    for i,ch in enumerate(S):
        if ch!=check[i%3]:
            valid=False
            break
elif S[0]=="c" and len(S)%6==5:
    check="cab"
    for i,ch in enumerate(S):
        if ch!=check[i%3]:
            valid=False
            break
else:
    valid=False
if valid:
    print((len(S)-1)//2)
else:
    print(-1)
