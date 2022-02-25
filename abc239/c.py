x1,y1,x2,y2=map(int, input().split())
set1=set()
set2=set()
for i in [-2,-1,1,2]:
    for j in [-2,-1,1,2]:
        if abs(i)==abs(j): continue
        set1.add((x1+i,y1+j))
        set2.add((x2+i,y2+j))
uni_set=set1|set2
if len(uni_set)==16:
    print("No")
else:
    print("Yes")
