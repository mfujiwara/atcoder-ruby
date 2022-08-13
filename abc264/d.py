S=input()
ret=0
for ch in "atcoder":
    index=S.index(ch)
    ret+=index
    if index==0:
        S=S[1:]
    elif index==len(S)-1:
        S=S[:-1]
    else:
        S=S[:index]+S[index+1:]
print(ret)
