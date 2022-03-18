S=input()
if S=="b":
    print(1,0)
    exit()
if S=="a":
    print(2,0)
    exit()
B=pow(10,5)+7
MOD=pow(10,9)+7
hashS=0
powB=[1]
for ch in S:
    hashS*=B
    hashS%=MOD
    hashS+=ord(ch)
    hashS%=MOD
    powB.append(powB[-1]*B%MOD)
F=[[0]*(pow(2,i-2) if i>=3 else 1) for i in range(23)]
F[1][0]=ord("b")
F[2][0]=ord("a")
ll=[0,1,1]
for n in range(3,23):
    ll.append(ll[-1]+ll[-2])
    for k in range(pow(2,n-2)):
        if k%2==0:
            F[n][k]=powB[ll[n-2]]*F[n-1][k//2]%MOD+F[n-2][k//4]
        else:
            F[n][k]=powB[ll[n-1]]*F[n-2][k//4]%MOD+F[n-1][k//2]
        F[n][k]%=MOD
        if F[n][k]==hashS:
            print(n,k)
            exit()
print("done")
