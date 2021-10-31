N=int(input())
A,B=map(int, input().split())
b1=True
b2=True
for _ in range(N-2):
    a,b=map(int, input().split())
    if b1 and A!=a and A!=b:
        b1=False
    if b2 and B!=a and B!=b:
        b2=False
    if not b1 and not b2:
        break
if b1 or b2:
    print("Yes")
else:
    print("No")
