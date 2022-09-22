S=input()
if S[0]=="0":
    cols=[
        S[6]=="0",
        S[3]=="0",
        S[1]=="0" and S[7]=="0",
        S[4]=="0",
        S[2]=="0" and S[8]=="0",
        S[5]=="0",
        S[9]=="0"
    ]
    status=0
    for c in cols:
        if status==0 and c==False:
            status=1
        elif status==1 and c==True:
            status=2
        elif status==2 and c==False:
            status=3
    if status==3:
        print("Yes")
    else:
        print("No")
else:
    print("No")
