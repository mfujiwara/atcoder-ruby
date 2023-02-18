K=int(input())
A,B=map(int, input().split())
for k in range(A,B+1):
    if k%K==0:
        print("OK")
        exit()
print("NG")
