N=int(input())
a_array=[]
b_array=[]
for i in range(N):
    a,b=map(int, input().split())
    a_array.append((a,i))
    b_array.append((b,i))
a_array=sorted(a_array)
b_array=sorted(b_array)
a0,ai0=a_array[0]
b0,bi0=b_array[0]
if ai0==bi0:
    a1,_=a_array[1]
    b1,_=b_array[1]
    print(min([a0+b0,max(a0,b1),max(b0,a1)]))
else:
    print(max(a0,b0))
