T=int(input())
for _ in range(T):
    strl,strr=input().split()
    lenl=len(strl)
    lenr=len(strr)
    l=int(strl)
    r=int(strr)
    if lenl==lenr:
        v=r-l+1
    elif strr[0]=="1":
        if strr[1]!="0":
            v=min(r-r//10,r-int(strr[1:]),r-l+1)
        else:
            #v=min(r-int("1"+strr[2:]),r-l+1)
            v=min(r-r//10,r-l+1)
    else:
        v=min(r-pow(10,lenr-1)+1,r-l+1)
    print(v)
