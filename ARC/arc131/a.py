A=int(input())
B=int(input())
if B%2==0:
    print(B//2*pow(10,10)+A)
else:
    print(B*10//2*pow(10,9)+A)
