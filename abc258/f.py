T=int(input())
for _ in range(T):
    B,K,Sx,Sy,Gx,Gy=map(int, input().split())
    smx=Sx%B
    smy=Sy%B
    gmx=Gx%B
    gmy=Gy%B
    ret=(abs(Sx-Gx)+abs(Sy-Gy))*K
    nearS=[]
    if smx==0 or smy==0:
        nearS.append((Sx,Sy,0))
    else:
        nearS.append((Sx-smx,Sy,smx*K))
        nearS.append((Sx+B-smx,Sy,(B-smx)*K))
        nearS.append((Sx,Sy-smy,smy*K))
        nearS.append((Sx,Sy+B-smy,(B-smy)*K))
    nearG=[]
    if gmx==0 or gmy==0:
        nearG.append((Gx,Gy,0))
    else:
        nearG.append((Gx-gmx,Gy,gmx*K))
        nearG.append((Gx+B-gmx,Gy,(B-gmx)*K))
        nearG.append((Gx,Gy-gmy,gmy*K))
        nearG.append((Gx,Gy+B-gmy,(B-gmy)*K))
    #print(nearS,nearG)
    for x0,y0,c0 in nearS:
        for x1,y1,c1 in nearG:
            if x0%B!=0 and x1%B!=0 and x0//B==x1//B and y0//B!=y1//B:
                v=c0+c1+abs(y0-y1)+min(x0%B+x1%B,B-x0%B+B-x1%B)
                ret=min(ret,v)
            elif y0%B!=0 and y1%B!=0 and y0//B==y1//B and x0//B!=x1//B:
                v=c0+c1+abs(x0-x1)+min(y0%B+y1%B,B-y0%B+B-y1%B)
                ret=min(ret,v)
            else:
                v=c0+c1+abs(x0-x1)+abs(y0-y1)
                ret=min(ret,v)
                #print("xyxy",x0,y0,x1,y1,"cost",c0+c1,v-c0-c1,v)
    print(ret)
