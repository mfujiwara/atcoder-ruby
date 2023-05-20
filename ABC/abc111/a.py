n=input()
m=""
for ch in n:
    if ch=="1":
        ch="9"
    elif ch=="9":
        ch="1"
    m+=ch
print(m)
