from collections import defaultdict
N=int(input())
a_array=list(map(int, input().split()))
a_count=defaultdict(int)
for a in a_array:
    a_count[a]+=1
b_array=list(map(int, input().split()))
b_count=defaultdict(int)
for b in b_array:
    b_count[b]+=1
c_array=list(map(int, input().split()))
c_count=defaultdict(int)
for c in c_array:
    c_count[c]+=1
ret=0
for c_val in c_count:
    c_num=c_count[c_val]
    b_val=b_array[c_val-1]
    a_num=a_count[b_val]
    ret+=c_num*a_num
print(ret)
