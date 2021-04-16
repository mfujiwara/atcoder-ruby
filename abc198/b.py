N=input()
while N!="0" and N[-1]=="0":
    N=N[:-1]
a=N[:len(N)//2]
b=N[::-1][:len(N)//2]
if a==b:
    print("Yes")
else:
    print("No")
