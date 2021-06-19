N=int(input())
v=0
for i in range(1,10**9):
    v+=i
    if v>=N:
        print(i)
        exit()
