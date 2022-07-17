N,X=map(int, input().split())
S=""
for i in range(26):
    ch=chr(ord("A")+i)
    S+=ch*N
print(S[X-1])
