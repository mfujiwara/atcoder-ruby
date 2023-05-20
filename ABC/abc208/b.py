P=int(input())
fn=[1,1]
for i in range(2,11):
    fn.append(fn[-1]*i)
ret=0
for i in range(10,0,-1):
    q,P=divmod(P,fn[i])
    ret+=q
print(ret)
