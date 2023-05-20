N=input()
o=0
e=0
for i,n in enumerate(N[::-1]):
    if i%2==0:
        o+=int(n)
    else:
        e+=int(n)
print(f"{e} {o}")
