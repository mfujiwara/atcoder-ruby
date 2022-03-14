import bisect
X=int(input())
array=[a**5 for a in range(-120,121)]
for b in range(-120,120):
    a=X+b**5
    index=bisect.bisect_left(array,a)
    if index<len(array) and array[index]==a:
        print(index-120,b)
        exit()
