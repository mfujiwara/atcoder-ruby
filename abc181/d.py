S=input()
if len(S)==1:
    if S=="8":
        print("Yes")
    else:
        print("No")
    exit()
if len(S)==2:
    if S in ["16","24","32","48","56","64","72","88","96","61","42","23","84","65","46","27","69"]:
        print("Yes")
    else:
        print("No")
    exit()
counts=[0]*10
for ch in S:
    counts[int(ch)]+=1
for i in range(1000,2001,8):
    t=str(i)
    t_counts=[0]*10
    for j in range(1,4):
        t_counts[int(t[j])]+=1
    valid=True
    for j in range(10):
        if counts[j]<t_counts[j]:
            valid=False
            break
    if valid:
        print("Yes")
        exit()
print("No")
