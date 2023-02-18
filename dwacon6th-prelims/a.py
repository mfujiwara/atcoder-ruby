N=int(input())
st=[]
for _ in range(N):
    s,t=input().split()
    t=int(t)
    st.append((s,t))
X=input()
ret=0
while st and st[-1][0]!=X:
    _,t=st.pop()
    ret+=t
print(ret)
