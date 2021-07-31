S=input()
if S=="zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()
if len(S)==26:
    able=[]
    s=S
    while True:
        s=list(s)
        able.append(s.pop())
        s="".join(s)
        able.sort()
        for a in able:
            t=s+a
            if t>S:
                print(t)
                exit()
for a in "abcdefghijklmnopqrstuvwxyz":
    if S.count(a)==0:
        print(S+a)
        exit()
