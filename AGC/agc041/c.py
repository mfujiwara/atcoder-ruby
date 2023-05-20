N=int(input())
if N<=2:
    print(-1)
elif N%3==0:
    # 3n
    for i in range(N//3):
        for j in range(3):
            print("."*i*3,end="")
            if j==0:
                print("aab",end="")
            elif j==1:
                print("d.b",end="")
            else:
                print("dcc",end="")
            print("."*(N-3*i-3))
else:
    r,q=divmod(N,4)
    if q!=0:
        r-=1
        q+=4
    for i in range(r):
        for j in range(4):
            print("."*i*4,end="")
            if j==0:
                print("aabc",end="")
            elif j==1:
                print("ddbc",end="")
            elif j==2:
                print("efgg",end="")
            else:
                print("efhh",end="")
            print("."*(N-4*i-4))
    if q==5:
        print("."*r*4,end="")
        print("aabba")
        print("."*r*4,end="")
        print("bcc.a")
        print("."*r*4,end="")
        print("b..cb")
        print("."*r*4,end="")
        print("a..cb")
        print("."*r*4,end="")
        print("abbaa")
    elif q==6:
        print("."*r*4,end="")
        print("aabc..")
        print("."*r*4,end="")
        print("ddbc..")
        print("."*r*4,end="")
        print("..aabc")
        print("."*r*4,end="")
        print("..ddbc")
        print("."*r*4,end="")
        print("bc..aa")
        print("."*r*4,end="")
        print("bc..dd")
    elif q==7:
        print("."*r*4,end="")
        print("aabbcc.")
        print("."*r*4,end="")
        print("dd.dd.a")
        print("."*r*4,end="")
        print("..d..da")
        print("."*r*4,end="")
        print("..d..db")
        print("."*r*4,end="")
        print("dd.dd.b")
        print("."*r*4,end="")
        print("..d..dc")
        print("."*r*4,end="")
        print("..d..dc")
