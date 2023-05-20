import sys
N=int(input())
n=N
while True:
    lose_range=((n+2)//2,n)
    if lose_range[0]<=1<=lose_range[1]:
        print("Aoki")
        sys.exit()
    n=lose_range[0]
    win_range=(n//2,n-1)
    if win_range[0]<=1<=win_range[1]:
        print("Takahashi")
        sys.exit()
    n=win_range[0]-1
