R,C,N=map(int, input().split())
memo=[]
for i in range(N):
    x1,y1,x2,y2=map(int, input().split())
    if (x1 in [0,R] or y1 in [0,C]) and (x2 in [0,R] or y2 in [0,C]):
        for x,y in [(x1,y1),(x2,y2)]:
            if x==0:
                memo.append((y,i))
            elif y==C:
                memo.append((C+x,i))
            elif x==R:
                memo.append((R+2*C-y,i))
            else:
                memo.append((2*R+2*C-x,i))
memo.sort()
stack=[]
while memo:
    p,i=memo.pop()
    if stack and stack[-1]==i:
        stack.pop()
    else:
        stack.append(i)
if stack:
    print("NO")
else:
    print("YES")
