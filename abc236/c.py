N,M=map(int, input().split())
s_array=input().split()
t_array=input().split()
t_ind=0
for s in s_array:
    if s==t_array[t_ind]:
        print("Yes")
        t_ind+=1
    else:
        print("No")
