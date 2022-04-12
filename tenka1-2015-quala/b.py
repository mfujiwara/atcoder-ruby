def calc(s):
    hour=int(s[0:2])
    minute=int(s[3:5])
    sec=int(s[6:8])
    millisec=int(s[9:12])
    ret=hour*60
    ret+=minute
    ret*=60
    ret+=sec
    ret*=1000
    ret+=millisec
    return ret*2
N=int(input())
start_end=[]
ss1=calc("20:00:00.000")
ee1=calc("23:50:00.000")
ss2=calc("20:00:00.000")
ee2=calc("23:50:00.000")
for _ in range(N):
    s,e=input().split()
    s=calc(s)
    e=calc(e)
    if s>=e:
        ss1=max(ss1,s+1)
        ee1=min(ee1,e+1999)
        ss2=max(ss2,s-1999)
        ee2=min(ee2,e-1)
    start_end.append((s,e))
#print(ss1,ee1,ss2,ee2)
for start,end in start_end:
    #print(start,end)
    if start>=end:
        print((end-start)//2+1000)
    else:
        isPre=ee1<start
        isPost=end<ss2
        isIn=start<ss2 and ee1<end
        if not isPre and not isPost and isIn:
            print((end-start)//2+1000)
        elif (isPre or isPost) and not isIn:
            print((end-start)//2)
        else:
            print(-1)
