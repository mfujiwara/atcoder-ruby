N=int(input())
ald=[]
for _ in range(N):
    a,l=input().split()
    ald.append((int(a),int(l),len(a)))
B=int(input())
ret=0
base=1
while ald:
    a,l,d=ald.pop()
    def calc(ll):
        if ll==1:
            return a
        ll,r=divmod(ll,2)
        v1=calc(ll)
        v2=v1*pow(10,ll*d,B)%B
        if r==0:
            v3=0
        else:
            v3=a*pow(10,ll*d*2,B)%B
        return (v1+v2+v3)%B
    v=calc(l)
    ret+=(v*base)%B
    ret%=B
    base*=pow(10,len(str(a))*l,B)
    base%=B
print(ret)
