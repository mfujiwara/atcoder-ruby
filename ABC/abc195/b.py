import math
A,B,W=map(int, input().split())
W*=1000
a=math.floor(W/A)
b=math.ceil(W/B)
if b<=a:
    print(f"{b} {a}")
else:
    print("UNSATISFIABLE")
