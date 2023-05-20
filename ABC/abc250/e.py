N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
a_first={}
b_first={}
for i in range(N):
    a=a_array[i]
    if a not in a_first:
        a_first[a]=i
    b=b_array[i]
    if b not in b_first:
        b_first[b]=i
a_ok=[N]*N
b_ok=[N]*N
for i in range(N):
    a=a_array[i]
    if a in b_first:
        a_ok[i]=b_first[a]
    if i>0:
        a_ok[i]=max(a_ok[i],a_ok[i-1])
    b=b_array[i]
    if b in a_first:
        b_ok[i]=a_first[b]
    if i>0:
        b_ok[i]=max(b_ok[i],b_ok[i-1])
# print(a_first)
# print(b_first)
# print(a_ok)
# print(b_ok)
Q=int(input())
for _ in range(Q):
    x,y=map(int, input().split())
    x-=1
    y-=1
    if y>=a_ok[x] and x>=b_ok[y]:
        print("Yes")
    else:
        print("No")
