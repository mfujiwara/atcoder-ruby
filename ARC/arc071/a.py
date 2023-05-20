n=int(input())
ord_a=ord("a")
counts=[0]*26
for ch in input():
    counts[ord(ch)-ord_a]+=1
for _ in range(n-1):
    c=[0]*26
    for ch in input():
        c[ord(ch)-ord_a]+=1
    for i in range(26):
        counts[i]=min(counts[i],c[i])
ret=""
for i,c in enumerate(counts):
    ret+=chr(i+ord_a)*c
print(ret)
