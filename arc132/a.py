n=int(input())
r_array=list(map(int, input().split()))
r_i_array=[(r,i) for i,r in enumerate(r_array)]
r_i_array.sort()
rij={}
for j in range(n):
    _,i=r_i_array[j]
    rij[i]=j
c_array=list(map(int, input().split()))
c_i_array=[(c,i) for i,c in enumerate(c_array)]
c_i_array.sort()
cij={}
for j in range(n):
    _,i=c_i_array[j]
    cij[i]=j
q=int(input())
for _ in range(q):
    r,c=map(int, input().split())
    v=rij[r-1]+cij[c-1]
    if v>=n-1:
        print("#",end="")
    else:
        print(".",end="")
print()
