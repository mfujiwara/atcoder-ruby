K=int(input())
k=""
for ch in bin(K)[2:]:
    if ch=="1":
        k+="2"
    else:
        k+="0"
print(k)
