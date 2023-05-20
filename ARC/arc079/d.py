K=int(input())
rets=[49]*50
r,q=divmod(K,50)
for i in range(50):
    if i<q:
        rets[i]+=(r+1)*50
        rets[i]-=(K-r-1)
    else:
        rets[i]+=r*50
        rets[i]-=(K-r)
print(50)
print(" ".join(map(str,rets)))
