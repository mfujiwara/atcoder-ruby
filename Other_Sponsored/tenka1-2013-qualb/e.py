import math
import random
def calc1(x,y,array):
    if len(array)==0:
        return 0
    nexts=(pow(10,10),-1)
    for i,ab in enumerate(array):
        a,b=ab
        d=pow(a-x,2)+pow(b-y,2)
        nexts=min(nexts,(d,i))
    x,y=array.pop(nexts[1])
    return calc1(x,y,array)+math.sqrt(nexts[0])
def calc2(x,y,array):
    if len(array)==0:
        return 0
    nexts1=(pow(10,10),-1)
    nexts2=(pow(10,10)+1,-1)
    for i,ab in enumerate(array):
        a,b=ab
        d=pow(a-x,2)+pow(b-y,2)
        v=(d,i)
        if v<nexts1:
            nexts1,nexts2=v,nexts1
        elif v<nexts2:
            nexts2=v
    if len(array)>2:
        x,y=array.pop(nexts2[1])
        return calc2(x,y,array)+math.sqrt(nexts2[0])
    else:
        x,y=array.pop(nexts1[1])
        return calc2(x,y,array)+math.sqrt(nexts1[0])
print(100)
array=[(0,0)]
for i in range(49):
    array.append((49-i,0))
    array.append((49-i-1,1))
array.append((10000,0))
for x,y in array:
    print(x,y)
#print(calc1(0,0,array[1:]))
#print(calc2(0,0,array[1:]))
