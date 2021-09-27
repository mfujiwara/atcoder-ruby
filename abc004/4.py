R,G,B=map(int, input().split())
def calc(start,num,base):
    start-=base
    if start<0:
        if start+num>0:
            s1=abs(start)
            s2=num+start-1
            return (s1+1)*s1//2 + (s2+1)*s2//2
        else:
            s=abs(start)
            t=abs(start+num-1)
            return (s+t)*num//2
    else:
        return (start+start+num-1)*num//2
ret=300*3*300
for r in range(-750,-99):
    for g in range(r+R,r+R+1500):
        cost=0
        # r-cost
        cost+=calc(r,R,-100)
        # g-cost
        cost+=calc(g,G,0)
        # b-cost
        b=max(g+G,100-B//2)
        cost+=calc(b,B,100)
        ret=min(ret,cost)
print(ret)
