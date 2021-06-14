N=int(input())
array=sorted(list(map(int, input().split())))
arr=[i+1 for i in range(N)]
if array==arr:
    print("Yes")
else:
    print("No")
