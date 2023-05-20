a=input()
b=input()
a_array=[0]*10
b_array=[0]*10
a_max=0
b_max=0
for ch in a:
    v=int(ch)
    a_array[v]+=1
    a_max=max(a_max,v)
for ch in b:
    v=int(ch)
    b_array[v]+=1
    b_max=max(b_max,v)
if b_max+a_max<10:
    print(a)
    print(b)
    exit()
ret_a=""
ret_b=""
for i in range(1,9):
    v=min(a_array[i],b_array[9-i])
    a_array[i]-=v
    b_array[9-i]-=v
    while a_array[a_max]==0 and a_max>0:
        a_max-=1
    while b_array[b_max]==0 and b_max>0:
        b_max-=1
    if a_max+b_max<10:
        v-=1
        a_array[i]+=1
        b_array[9-i]+=1
        a_max=max(a_max,i)
        b_max=max(b_max,9-i)
    ret_a+=str(i)*v
    ret_b+=str(9-i)*v
a9=0
b9=0
if len(a)>len(b):
    a9=min(a_array[9],len(a)-len(b))
    a_array[9]-=a9
    while a_array[a_max]==0 and a_max>0:
        a_max-=1
    if a_max+b_max<10:
        a_array[9]+=1
        a9-=1
        a_max=9
elif len(b)>len(a):
    b9=min(b_array[9],len(b)-len(a))
    b_array[9]-=b9
    while b_array[b_max]==0 and b_max>0:
        b_max-=1
    if a_max+b_max<10:
        b_array[9]+=1
        b9-=1
        b_max=9
ret_a="9"*a9+ret_a
ret_b="9"*b9+ret_b
for i in range(10,19):
    for j in range(i-9,10):
        v=min(a_array[j],b_array[i-j])
        a_array[j]-=v
        b_array[i-j]-=v
        ret_a+=str(j)*v
        ret_b+=str(i-j)*v
rest_a=""
rest_b=""
for i in range(10):
    rest_a+=str(i)*a_array[i]
    rest_b+=str(i)*b_array[i]
head_a=""
head_b=""
if len(rest_a)>len(rest_b):
    head_a=rest_a[len(rest_b):]
    rest_a=rest_a[:len(rest_b)]
elif len(rest_b)>len(rest_a):
    head_b=rest_b[len(rest_a):]
    rest_b=rest_b[:len(rest_a)]
ret_a=head_a+ret_a+rest_a
ret_b=head_b+ret_b+rest_b
print(ret_a)
print(ret_b)
