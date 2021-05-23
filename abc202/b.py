S=input()
INV_S=""
for ch in S:
    if ch=="6":
        INV_S+="9"
    elif ch=="9":
        INV_S+="6"
    else:
        INV_S+=ch
print(INV_S[::-1])
