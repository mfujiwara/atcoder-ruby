N,K,Q=map(int, input().split())
a_array=list(map(int, input().split()))
l_array=list(map(int, input().split()))
for l in l_array:
    if l==K:
        a=a_array[l-1]
        if a<N:
            a_array[l-1]+=1
    else:
        if a_array[l-1]+1<a_array[l]:
            a_array[l-1]+=1
print(*a_array)
