from collections import defaultdict
N=int(input())
array=list(map(int, input().split()))
counts=defaultdict(int)
for a in array:
    counts[a%200]+=1
ret=0
for c in counts:
    v=counts[c]
    r=(v*(v-1))//2
    ret+=r
print(ret)
