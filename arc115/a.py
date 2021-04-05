N,M=map(int, input().split())
odd=0
even=0
for _ in range(N):
    s=input()
    if s.count("0")%2==0:
        even+=1
    else:
        odd+=1
print(odd*even)    
