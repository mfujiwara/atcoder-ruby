array=list(map(int,list(input())))
ret=True
for i in range(len(array)-1):
    if array[i]<=array[i+1]:
        ret=False
        break
print("Yes" if ret else "No")
