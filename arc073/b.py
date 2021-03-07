import bisect
N,W=map(int, input().split())
w1,v1=map(int, input().split())
w2=w1+1
w3=w1+2
w4=w1+3
w1_array=[v1]
w2_array=[]
w3_array=[]
w4_array=[]
for _ in range(N-1):
    w,v=map(int, input().split())
    if w==w1:
        w1_array.append(v)
    elif w==w2:
        w2_array.append(v)
    elif w==w3:
        w3_array.append(v)
    else:
        w4_array.append(v)
w1_sums=[0]
w2_sums=[0]
w3_sums=[0]
w4_sums=[0]
for v in sorted(w1_array)[::-1]:
    w1_sums.append(w1_sums[-1]+v)
for v in sorted(w2_array)[::-1]:
    w2_sums.append(w2_sums[-1]+v)
for v in sorted(w3_array)[::-1]:
    w3_sums.append(w3_sums[-1]+v)
for v in sorted(w4_array)[::-1]:
    w4_sums.append(w4_sums[-1]+v)
ret=0
for i in range(min(W//w1+1,len(w1_sums))):
    W2=W-w1*i
    for j in range(min(W2//w2+1,len(w2_sums))):
        W3=W2-w2*j
        for k in range(min(W3//w3+1,len(w3_sums))):
            W4=W3-w3*k
            l=min(W4//w4,len(w4_sums)-1)
            r=w1_sums[i]+w2_sums[j]+w3_sums[k]+w4_sums[l]
            ret=max(ret,r)
print(ret)
