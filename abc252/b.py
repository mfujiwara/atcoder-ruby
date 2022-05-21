N,K=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=set(map(int, input().split()))
a_array=sorted([(a,i+1) for i,a in enumerate(a_array)])
v=a_array[-1][0]
while a_array and a_array[-1][0]==v:
    a,i=a_array.pop()
    if i in b_array:
        print("Yes")
        exit()
print("No")
