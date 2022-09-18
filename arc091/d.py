N=int(input())
grundy=0
for _ in range(N):
    a,k=map(int, input().split())
    while a%k:
        a-=a%k+(-(a%k))%((a+k-1)//k)
    grundy^=a//k
if grundy:
    print("Takahashi")
else:
    print("Aoki")
