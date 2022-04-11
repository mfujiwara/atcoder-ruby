N=int(input())
array=list(map(int, input().split()))
if array[-1]>=array[-2]+2:
    print("Alice")
elif (array[-1]+N)%2==0:
    print("Alice")
else:
    print("Bob")
