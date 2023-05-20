S=input()
t=0
array=[]
for ch in S[::-1]:
    if ch=="+":
        t+=1
    elif ch=="-":
        t-=1
    else:
        array.append(t)
array.sort()
ret=sum(array[len(array)//2:])-sum(array[:len(array)//2])
print(ret)
