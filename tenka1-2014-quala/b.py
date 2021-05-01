S=input()
kaburin=5
back=[0]*(len(S)+10)
comboup=[0]*(len(S)+10)
stop=0
combo=0
damage=0
for i,ch in enumerate(S):
    kaburin+=back[i]
    combo+=comboup[i]
    if stop>0:
        stop-=1
        continue
    if ch=="N":
        if kaburin>0:
            kaburin-=1
            damage+=10+combo//10
            comboup[i+2]+=1
            back[i+7]+=1
    elif ch=="C":
        if kaburin>2:
            kaburin-=3
            stop+=2
            damage+=50+combo//10*5
            comboup[i+4]+=1
            back[i+9]+=3
print(damage)
