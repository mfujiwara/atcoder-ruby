N,X=input().split()
array=list(input().split())
deleted_array=[array[i] for i in range(int(N)) if array[i]!=X ]
print(" ".join(deleted_array))
