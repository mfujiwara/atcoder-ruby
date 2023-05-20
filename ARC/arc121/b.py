N=int(input())
dogs_r=[]
dogs_g=[]
dogs_b=[]
for i in range(2*N):
    a,c=input().split()
    a=int(a)
    if c=="R":
        dogs_r.append(a)
    elif c=="G":
        dogs_g.append(a)
    else:
        dogs_b.append(a)
if len(dogs_r)%2==0 and len(dogs_g)%2==0:
    print(0)
    exit()
dogs_r=sorted(dogs_r)
dogs_g=sorted(dogs_g)
dogs_b=sorted(dogs_b)
if len(dogs_r)%2==0:
    dogs_r,dogs_b=dogs_b,dogs_r
if len(dogs_g)%2==0:
    dogs_g,dogs_b=dogs_b,dogs_g
ret=abs(dogs_r[0]-dogs_g[0])
if dogs_r[0]>dogs_g[0]:
    r_i,g_i=0,1
else:
    r_i,g_i=1,0
while r_i<len(dogs_r) and g_i<len(dogs_g):
    ret=min(ret,abs(dogs_r[r_i]-dogs_g[g_i]))
    if dogs_r[r_i]>dogs_g[g_i]:
        g_i+=1
    else:
        r_i+=1
if len(dogs_b)==0:
    print(ret)
    exit()

ret_rb1=(1<<60,-1)
ret_rb2=(1<<60,-1)
ret_gb1=(1<<60,-1)
ret_gb2=(1<<60,-1)
r_i=0
g_i=0
for b_i,dog_b in enumerate(dogs_b):
    while r_i<len(dogs_r)-1 and dogs_r[r_i+1]<dog_b:
        r_i+=1
    while g_i<len(dogs_g)-1 and dogs_g[g_i+1]<dog_b:
        g_i+=1
    v_r=(abs(dog_b-dogs_r[r_i]),b_i)
    if r_i<len(dogs_r)-1:
        v_r=min(v_r, (abs(dog_b-dogs_r[r_i+1]),b_i))
    v_g=(abs(dog_b-dogs_g[g_i]),b_i)
    if g_i<len(dogs_g)-1:
        v_g=min(v_g, (abs(dog_b-dogs_g[g_i+1]),b_i))

    if v_r<ret_rb1:
        ret_rb1,ret_rb2=v_r,ret_rb1
    elif v_r<ret_rb2:
        ret_rb2=v_r
    if v_g<ret_gb1:
        ret_gb1,ret_gb2=v_g,ret_gb1
    elif v_g<ret_gb2:
        ret_gb2=v_g
if ret_rb1[1]!=ret_gb1[1]:
    ret=min(ret,ret_rb1[0]+ret_gb1[0])
else:
    ret=min(ret,ret_rb1[0]+ret_gb2[0])
    ret=min(ret,ret_rb2[0]+ret_gb1[0])
print(ret)
