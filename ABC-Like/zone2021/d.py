S=input()
ret=[]
ret_rev=[]
reverse=False
for ch in S:
    if ch=="R":
        reverse=not reverse
    else:
        if reverse:
            if len(ret_rev)==0:
                ret_rev=[ch]
            elif ret_rev[-1]==ch:
                ret_rev.pop()
            else:
                ret_rev.append(ch)
        else:
            if len(ret)==0:
                ret=[ch]
            elif ret[-1]==ch:
                ret.pop()
            else:
                ret.append(ch)
ret=ret[::-1]
ret_rev=ret_rev[::-1]
while ret and ret_rev and ret[-1]==ret_rev[-1]:
    ret.pop()
    ret_rev.pop()
r=ret+ret_rev[::-1] if reverse else ret_rev+ret[::-1]
print("".join(r))
