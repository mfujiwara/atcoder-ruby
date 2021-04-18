A,B=map(int, input().split())
for i in range(B-A,0,-1):
    a=(A+i-1)//i
    b=B//i
    if a<b:
        print(i)
        exit()
