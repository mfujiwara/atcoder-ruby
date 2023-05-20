N=int(input())
even_odd={}
array=[]
for i in range(N):
    a=int(input())
    even_odd[a]=i%2
    array.append(a)
r=0
for i,a in enumerate(sorted(array)):
    if i%2!=even_odd[a]:
        r+=1
print(r//2)
