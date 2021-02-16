T=int(input())
for _ in range(T):
    l,r=map(int, input().split())
    max_v=r-l
    if max_v<l:
        print(0)
        continue
    print((max_v-l+1)*(max_v-l+2)//2)
