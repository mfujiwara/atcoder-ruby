S=input()
s=set()
for i,j,k in [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]:
    s.add(S[i]+S[j]+S[k])
print(len(s))
