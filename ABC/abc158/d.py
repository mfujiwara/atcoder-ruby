S=input()
Q=int(input())
reverse=False
head=""
tail=""
for _ in range(Q):
    q=input().split()
    if q[0]=="1":
        reverse=not reverse
    else:
        _,f,c=q
        if (f=="1" and not reverse) or (f=="2" and reverse):
            head+=c
        else:
            tail+=c
if reverse:
    print(tail[::-1]+S[::-1]+head)
else:
    print(head[::-1]+S+tail)
