import sys
K=int(input())
array=list(map(int, input().split()))
min_a=2
max_a=2
for a in array[::-1]:
    # a*n>=min_a
    min_a=(min_a+a-1)//a*a
    # a*(n+1)-1<=max_a
    max_a=(max_a//a+1)*a-1
    if min_a>max_a:
        print("-1")
        sys.exit()
print("{} {}".format(min_a,max_a))
