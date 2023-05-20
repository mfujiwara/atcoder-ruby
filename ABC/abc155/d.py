N,K=map(int, input().split())
array=list(map(int, input().split()))
m_array=[]
p_array=[]
zero_count=0
maxi=0
for a in array:
    if a==0:
        zero_count+=1
    elif a>0:
        p_array.append(a)
        maxi=max(maxi,a)
    else:
        m_array.append(-a)
        maxi=max(maxi,-a)
m_array.sort()
p_array.sort()
m_c=len(m_array)*len(p_array)
z_c=zero_count*(len(m_array)+len(p_array))+zero_count*(zero_count-1)//2
p_c=len(m_array)*(len(m_array)-1)//2+len(p_array)*(len(p_array)-1)//2
if m_c>=K:
    left=-pow(maxi,2)-1
    right=0
elif m_c+z_c>=K:
    print(0)
    exit()
else:
    left=0
    right=pow(maxi,2)+1
while True:
    if left+1==right:
        print(right)
        exit()
    mid=(left+right)//2
    k=0
    if mid==0:
        k=m_c+z_c
    elif mid>0:
        k=m_c+z_c
        r=len(p_array)
        k2=0
        for a in p_array:
            while r>0 and p_array[r-1]*a>mid:
                r-=1
            if r>0 and p_array[r-1]>=a:
                k2+=r-1
            else:
                k2+=r
        k+=k2//2
        r=len(m_array)
        k2=0
        for a in m_array:
            while r>0 and m_array[r-1]*a>mid:
                r-=1
            if r>0 and m_array[r-1]>=a:
                k2+=r-1
            else:
                k2+=r
        k+=k2//2
    else:
        r=len(p_array)
        for a in m_array[::-1]:
            while r>0 and p_array[-r]*a<-mid:
                r-=1
            k+=r
    if k<K:
        left=mid
    else:
        right=mid
