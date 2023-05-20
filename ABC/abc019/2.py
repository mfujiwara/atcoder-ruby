s=input()
stack=[["_",0]]
for ch in s:
    if stack[-1][0]==ch:
        stack[-1][1]+=1
    else:
        stack.append([ch,1])
rets=[]
for ch,n in stack:
    if n!=0:
        rets.append(ch+str(n))
print("".join(rets))
