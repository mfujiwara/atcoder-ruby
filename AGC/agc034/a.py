N,A,B,C,D=map(int, input().split())
S=input()
if C<D:
    if B<C:
        pre=True
        for ch in S[A:D]:
            now = ch=="."
            if not pre and not now:
                print("No")
                exit()
            pre=now
    else:
        pre=True
        for ch in S[A:C]:
            now = ch=="."
            if not pre and not now:
                print("No")
                exit()
            pre=now
        pre=True
        for ch in S[B:D]:
            now = ch=="."
            if not pre and not now:
                print("No")
                exit()
            pre=now
else:
    pre=True
    for ch in S[A:C]:
        now = ch=="."
        if not pre and not now:
            print("No")
            exit()
        pre=now
    count=1 if S[B-2]=="." else 0
    for ch in S[B-1:D+1]:
        count = count+1 if ch=="." else 0
        if count==3:
            break
    if count<3:
        print("No")
        exit()
print("Yes")
