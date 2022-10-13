a,b,c=map(int, input().split())
# a^0.5 + b^0.5 < c^0.5
# a+b + 2*(a*b)^0.5 < c
# 2*(a*b)^0.5 < c-a-b
if c-a-b>0 and 4*a*b<pow(c-a-b,2):
    print("Yes")
else:
    print("No")
