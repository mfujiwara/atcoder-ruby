N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
sorted_a=sorted(a_array)
sorted_b=sorted(b_array)
for i in range(N):
    if sorted_a[i]>sorted_b[i]:
        print("No")
        exit()
for i in range(N-1):
    if sorted_a[i+1]<=sorted_b[i]:
        print("Yes")
        exit() 
b_sorted2org={}
for i in range(N):
    b_sorted2org[sorted_b[i]]=i
ab_array=[]
for i in range(N):
    ab_array.append((a_array[i],b_array[i]))
sorted_ab=sorted(ab_array)
sorted_a2org_b=[b_sorted2org[b] for _,b in sorted_ab]
m=1
i=sorted_a2org_b[0]
while i!=0:
    i=sorted_a2org_b[i]
    m+=1
if m<N:
    print("Yes")
else:
    print("No")
