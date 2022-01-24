X=input()+"o"
i=0
while i<len(X):
    if X[i]=="c" and X[i+1]=="h":
        i+=2
    elif X[i] in ["o","k","u"]:
        i+=1
    else:
        print("NO")
        exit()
print("YES")
