s=0
y=100
for i in range(1,101):
    if s+i*2>1500:
        y+=200
        print(f"{i} {y}")
        s=i*2
    else:
        print(f"{s+i} {y}")
        s+=i*2
