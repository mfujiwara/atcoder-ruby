N=int(input())
array=list(map(int, input().split()))
total=0
for a in array:
    total^=a
if total in array or N%2==1:
    print("Win")
else:
    print("Lose")
