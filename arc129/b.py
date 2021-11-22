N=int(input())
min_r=pow(10,10)
max_l=0
for _ in range(N):
    l,r=map(int, input().split())
    min_r=min(min_r,r)
    max_l=max(max_l,l)
    print(max(0,(max_l-min_r+1)//2))
