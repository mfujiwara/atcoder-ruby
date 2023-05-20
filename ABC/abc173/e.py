MOD=10**9+7
N,K=map(int, input().split())
array=list(map(int, input().split()))
array=sorted(array, key=lambda e: -abs(e))
kouho=[]
last_plus=-1
last_minus=-1
next_plus=-1
next_minus=-1
minus_count=0
for i,a in enumerate(array):
    if i<K:
        kouho.append(a)
        if a>0:
            last_plus=i
        elif a<0:
            last_minus=i
            minus_count+=1
        else:
            print(0)
            exit()
    elif minus_count%2==0:
        break
    else:
        if a>0:
            if next_plus<0:
                next_plus=i
        else:
            if next_minus<0:
                next_minus=i
        if next_minus>0 and next_plus>0:
            break
if last_plus<0 and next_plus<0 and K%2==1:
    kouho=array[-K:]
    ret=1
    for a in kouho:
        ret*=a
        ret%=MOD
    print(ret)
elif next_minus<0 and next_plus<0:
    ret=1
    for a in kouho:
        ret*=a
        ret%=MOD
    print(ret)
elif next_minus<0 or last_plus<0:
    ret=1
    for i,a in enumerate(kouho):
        if i==last_minus:
            ret*=array[next_plus]
        else:
            ret*=a
        ret%=MOD
    print(ret)
elif next_plus<0 or last_minus<0:
    ret=1
    for i,a in enumerate(kouho):
        if i==last_plus:
            ret*=array[next_minus]
        else:
            ret*=a
        ret%=MOD
    print(ret)
else:
    # last_plus->next_minus or last_minus->next_plus
    # next_minus/last_plus or next_plus/last_minus
    if array[next_minus]*array[last_minus]>=array[next_plus]*array[last_plus]:
        ret=1
        for i,a in enumerate(kouho):
            if i==last_plus:
                ret*=array[next_minus]
            else:
                ret*=a
            ret%=MOD
        print(ret)
    else:
        ret=1
        for i,a in enumerate(kouho):
            if i==last_minus:
                ret*=array[next_plus]
            else:
                ret*=a
            ret%=MOD
        print(ret)
