S=input()
ret=0
count_b=0
for i,ch in enumerate(S):
    if ch=="W":
        ret+=count_b
    else:
        count_b+=1
print(ret)
