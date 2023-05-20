C=input()
length=len(C)
if C.count("_")==len(C):
    print(C)
    exit()
prefix=0
suffix=0
while C[prefix]=="_":
    prefix+=1
while C[-1-suffix]=="_":
    suffix+=1
truncate_C=C[prefix:length-suffix]
is_snake=True
is_camel=True
snake=False
for i,ch in enumerate(truncate_C):
    if i==0:
        if "0"<=ch<="9" or "A"<=ch<="Z":
            is_snake=False
            is_camel=False
            break
    else:
        if snake:
            snake=False
            if "0"<=ch<="9" or "A"<=ch<="Z" or ch=="_":
                is_snake=False
                if not is_camel: break
        else:
            if ch=="_":
                is_camel=False
                snake=True
                if not is_snake: break
            elif "A"<=ch<="Z":
                is_snake=False
                if not is_camel: break
                
if is_snake:
    ret=""
    snake=False
    for ch in truncate_C:
        if ch=="_":
            snake=True
        elif snake:
            ret+=ch.upper()
            snake=False
        else:
            ret+=ch
    print("_"*prefix+ret+"_"*suffix)
elif is_camel:
    ret=""
    for ch in truncate_C:
        if "A"<=ch<="Z":
            ret+="_"+ch.lower()
        else:
            ret+=ch
    print("_"*prefix+ret+"_"*suffix)
else:
    print(C)
