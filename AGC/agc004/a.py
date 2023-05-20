A,B,C=map(int, input().split())
e1=[]
e2=[]
e1.append(A//2)
e2.append(A-e1[-1])
e1.append(B//2)
e2.append(B-e1[-1])
e1.append(C//2)
e2.append(C-e1[-1])
diffs = [
    (e2[0]-e1[0])*B*C,
    (e2[1]-e1[1])*C*A,
    (e2[2]-e1[2])*A*B,
]
print(min(diffs))
