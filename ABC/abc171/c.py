N=int(input())
l=1
maxi=26
while N>maxi:
    l+=1
    maxi+=pow(26,l)
diff=maxi-N
array=[]
while diff>0:
    diff,r=divmod(diff,26)
    array.append(r)
rets=["z"]*l
for i,d in enumerate(array):
    rets[i]=chr(ord("z")-d)
print("".join(rets[::-1]))
