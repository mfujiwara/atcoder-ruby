DAY=24*60
N=int(input())
se=[]
for _ in range(N):
    s,e=input().split()
    sh,sm=map(int, s.split(":"))
    eh,em=map(int, e.split(":"))
    s=sh*60+sm
    e=eh*60+em
    se.append((s,e))
se.sort(key=lambda e: (e[0],-e[1]))
dp=[-1]*pow(2,N)
seats=[[0,DAY*2-1] for _ in range(N+1)]
for s,e in se:
    for i,seat in enumerate(seats):
        if seat[0]<=s and e<=seat[1]:
            seat[0]=e
            seat[1]=min(seat[1],s+DAY)
            seats.sort(key=lambda e: (e[1],-e[0]))
            break
print(seats.index([0,DAY*2-1]))
