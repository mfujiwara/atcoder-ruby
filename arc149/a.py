N,M=map(int, input().split())
ret=-1
for i in range(1,10):
    d=1
    x=i%M
    done=set()
    done.add(x)
    while x>0:
        x=x*10+i
        d+=1
        x%=M
        if x in done or d>N:
            break
        done.add(x)
    #print(i,d,x)
    if x==0 and d<=N:
        ret=max(ret,int(str(i)*(N//d*d)))
print(ret)
