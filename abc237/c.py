S=input()
head=0
tail=0
for i in range(len(S)):
    if S[i]=="a":
        head+=1
    else:
        break
for i in range(len(S)-1,-1,-1):
    if S[i]=="a":
        tail+=1
    else:
        break
if head<=tail:
    T="a"*(tail-head)+S
    invT=T[::-1]
    if T==invT:
        print("Yes")
    else:
        print("No")
else:
    print("No")
