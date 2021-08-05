N=int(input())
a_array=sorted(list(map(int, input().split())))
b_array=sorted(list(map(int, input().split())))
print(sum([abs(a_array[i]-b_array[i]) for i in range(N)]))
