N=int(input())
array=list(map(int, input().split()))
free=0
colors=set()
for a in array:
    if a<=399:
        colors.add("hai")
    elif a<=799:
        colors.add("cha")
    elif a<=1199:
        colors.add("midori")
    elif a<=1599:
        colors.add("mizu")
    elif a<=1999:
        colors.add("ao")
    elif a<=2399:
        colors.add("ki")
    elif a<=2799:
        colors.add("dai")
    elif a<=3199:
        colors.add("aka")
    else:
        free+=1
print(max(1,len(colors)),len(colors)+free)
