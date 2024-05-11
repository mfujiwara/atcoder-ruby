A,B=map(int, input().split())
if A==B:
    print("1.000")
    exit()
if B==0:
    print("0.000")
    exit()
ret=B*10000//A
if ret%10>=5:
    ret//=10
    ret+=1
else:
    ret//=10
ret=str(ret)
print("0." + ret)
