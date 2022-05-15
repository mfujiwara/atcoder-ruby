N,A,B=map(int, input().split())
s1=""
s2=""
for i in range(N):
    if i%2==0:
        s1+="."*B
        s2+="#"*B
    else:
        s1+="#"*B
        s2+="."*B
for i in range(N):
    for j in range(A):
        if i%2==0:
            print(s1)
        else:
            print(s2)
