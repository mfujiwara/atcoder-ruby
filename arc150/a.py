T=int(input())
for _ in range(T):
    N,K=map(int, input().split())
    N+=2
    S="0"+input()+"0"
    first1=N
    last1=-1
    for i,ch in enumerate(S):
        if ch=="1":
            first1=min(first1,i)
            last1=max(last1,i)
    if first1<N:
        if last1-first1+1>K:
            print("No")
            continue
        if "0" in S[first1:last1+1]:
            print("No")
            continue
        if last1-first1+1==K:
            print("Yes")
            continue
        diff=K-(last1-first1+1)
        if S[first1-1]=="0":
            if last1+diff<N and S[last1+1:last1+1+diff]=="?"*diff:
                print("Yes")
            else:
                print("No")
        elif S[last1+1]=="0":
            if first1-diff>=0 and S[first1-diff:first1]=="?"*diff:
                print("Yes")
            else:
                print("No")
        else:
            c=0
            i=0
            while last1+1+i<N and S[last1+1+i]=="?":
                c+=1
                i+=1
            i=0
            while first1-1-i>=0 and S[first1-1-i]=="?":
                c+=1
                i+=1
            if c==diff:
                print("Yes")
            else:
                print("No")
    else:
        c=0
        count=0
        for ch in S:
            if ch=="?":
                c+=1
            else:
                if c==K:
                    count+=1
                elif c>K:
                    count+=2
                if count>1:
                    break
                c=0
        if count==1:
            print("Yes")
        else:
            print("No")
