import math
A,B=map(int, input().split())
if A<B:
    A,B=B,A
N=int(input())
for _ in range(N):
    c,d=map(int, input().split())
    if c<d:
        c,d=d,c
    if A<=c and B<=d:
        # 縦横一致して入る
        print("YES")
        continue
    def calc():
        left=0
        right=math.acos(B/math.hypot(A,B))
        while right-left>pow(10,-9):
            mid=(right+left)/2
            w=math.cos(mid)*A+math.sin(mid)*B
            h=math.sin(mid)*A+math.cos(mid)*B
            if w<=c and h<=d:
                return True
            if h<d:
                left=mid
            else:
                right=mid
        return False
    if calc():
        print("YES")
    else:
        print("NO")
