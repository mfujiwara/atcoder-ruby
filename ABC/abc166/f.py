N,A,B,C=map(int, input().split())
if A+B+C!=2:
    rets=[]
    for _ in range(N):
        s=input()
        if s=="AB":
            if A==0 and B==0:
                print("No")
                exit()
            if A<B:
                rets.append("A")
                A+=1
                B-=1
            else:
                rets.append("B")
                A-=1
                B+=1
        elif s=="AC":
            if A==0 and C==0:
                print("No")
                exit()
            if A<C:
                rets.append("A")
                A+=1
                C-=1
            else:
                rets.append("C")
                A-=1
                C+=1
        else:
            if B==0 and C==0:
                print("No")
                exit()
            if B<C:
                rets.append("B")
                B+=1
                C-=1
            else:
                rets.append("C")
                B-=1
                C+=1
    print("Yes")
    for r in rets:
        print(r)
else:
    ss=[input() for _ in range(N)]
    rets=[]
    for i,s in enumerate(ss):
        if s=="AB":
            if A==0 and B==0:
                print("No")
                exit()
            if A<B:
                rets.append("A")
                A+=1
                B-=1
            elif A>B:
                rets.append("B")
                A-=1
                B+=1
            else:
                if i==N-1 or ss[i+1]=="AB" or ss[i+1]=="AC":
                    rets.append("A")
                    A+=1
                    B-=1
                else:
                    rets.append("B")
                    A-=1
                    B+=1
        elif s=="AC":
            if A==0 and C==0:
                print("No")
                exit()
            if A<C:
                rets.append("A")
                A+=1
                C-=1
            elif A>C:
                rets.append("C")
                A-=1
                C+=1
            else:
                if i==N-1 or ss[i+1]=="AB" or ss[i+1]=="AC":
                    rets.append("A")
                    A+=1
                    C-=1
                else:
                    rets.append("C")
                    A-=1
                    C+=1
        else:
            if B==0 and C==0:
                print("No")
                exit()
            if B<C:
                rets.append("B")
                B+=1
                C-=1
            elif B>C:
                rets.append("C")
                B-=1
                C+=1
            else:
                if i==N-1 or ss[i+1]=="AB" or ss[i+1]=="BC":
                    rets.append("B")
                    B+=1
                    C-=1
                else:
                    rets.append("C")
                    B-=1
                    C+=1
    print("Yes")
    for r in rets:
        print(r)
