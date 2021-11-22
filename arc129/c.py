maxi=0
for M in range(1):
    N=int(input())
    def calc(n):
        left=1
        right=n+1
        while left+1!=right:
            mid=(left+right)//2
            v=mid*(mid+1)//2
            if v<=n:
                left=mid
            else:
                right=mid
        return left
    mods=[]
    ret=""
    c=1
    while N>0:
        v=calc(N)
        ret+="7"*v
        if c<7:
            new_mods=[]
            xxx=[i for i in range(1,7)]
            for mod in mods:
                x=mod*pow(10,v+1)%7
                new_mods.append(x)
                if 7-x in xxx:
                    xxx.remove(7-x)
            # print("v",v)
            # print("mods    ",mods)
            # print("new_mods",new_mods)
            # print("xxx",xxx)
            x=xxx[0]
            for i in range(len(new_mods)):
                new_mods[i]+=x
            new_mods.append(x)
            mods=new_mods
            ret+=str(x)
        N-=v*(v+1)//2
        c+=1
    maxi=max(maxi,c)
    print(ret)
