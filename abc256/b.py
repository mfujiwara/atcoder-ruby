N=int(input())
array=list(map(int, input().split()))
p=0
while array and p+array[-1]<4:
    p+=array.pop()
print(len(array))
