import math
XYR=input().split()
for i in range(3):
    if "." in XYR[i]:
        x1,x2=XYR[i].split(".")
        while len(x2)<4:
            x2+="0"
        XYR[i]=int(x1)*10000+int(x2)
    else:
        XYR[i]=int(XYR[i])*10000
X,Y,R=XYR
ret=0
for x in range((X-R+9999)//10000*10000,(X+R+10000)//10000*10000,10000):
    h=int(math.sqrt(R**2-(X-x)**2))-1
    while pow(h+1,2)+pow(X-x,2)<=pow(R,2):
        h+=1
    top=(Y+h)//10000
    bottom=(Y-h+9999)//10000
    c=max(top-bottom+1,0)
    ret+=c
print(ret)
