S=input()
T=input()
s_counts=[["_",1]]
for ch in S:
    if s_counts[-1][0]==ch:
        s_counts[-1][1]+=1
    else:
        s_counts.append([ch,1])
t_counts=[["_",1]]
for ch in T:
    if t_counts[-1][0]==ch:
        t_counts[-1][1]+=1
    else:
        t_counts.append([ch,1])
if len(s_counts)!=len(t_counts):
    print("No")
    exit()
for i in range(len(s_counts)):
    s_ch,sc=s_counts[i]
    t_ch,tc=t_counts[i]
    if s_ch!=t_ch or (sc==1 and tc>=2) or (sc>tc):
        print("No")
        exit()
print("Yes")
