import math
N=int(input())
if N==1:
    print("Yes")
    exit()
ab=[]
A,B=map(int, input().split())
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=A
    b-=B
    ab.append((a,b))
ab=sorted(ab)
#print(f"ab: {ab}")
cd=[]
for _ in range(N):
    c,d=map(int, input().split())
    cd.append((c,d))
for i,CD in enumerate(cd):
    C,D=CD
    #print(f"CD: {C} {D}")
    verify_cd=[]
    for j in range(N):
        if j==i: continue
        c,d=cd[j]
        verify_cd.append((c-C,d-D))
    #print(f"verify: {verify_cd}")
    a,b=ab[0]
    for c,d in verify_cd:
        if math.hypot(a,b)!=math.hypot(c,d): continue
        # cx-dy=a, cy+dx=b
        # cdx-ddy=ad ccy+cdx=bc
        # ddy+ccy=bc-ad
        # y=(bc-ad)//(dd+cc)
        # ccx-cdy=ac cdy+ddx=bd
        # ccx+ddx=ac+bd
        # x=(ac+bd)//(cc+dd)
        x=(a*c+b*d)
        y=(b*c-a*d)
        rotate_cd=[]
        for cc,dd in verify_cd:
            rotate_c=0 if c==0 and d==0 else (cc*x-dd*y)/(c*c+d*d)
            rotate_d=0 if c==0 and d==0 else (cc*y+dd*x)/(c*c+d*d)
            rotate_cd.append((rotate_c,rotate_d))
        rotate_cd=sorted(rotate_cd)
        #print(f"cd: {rotate_cd}")
        if rotate_cd==ab:
            print("Yes")
            exit()
print("No")
