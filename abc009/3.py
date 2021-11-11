import collections
from itertools import count
N,K=map(int, input().split())
S=input()
T=""
ord_a=ord("a")
counts1=[0]*26
counts2=[0]*26
for ch in S:
    counts1[ord(ch)-ord_a]+=1
    counts2[ord(ch)-ord_a]+=1
fix_d=0
chars=sorted(list(S))
for i in range(N):
    #print(fix_d, diffs,T,chars)
    counts1[ord(S[i])-ord_a]-=1
    for k in range(len(chars)):
        ch=chars[k]
        if ch==S[i]:
            T+=ch
            counts2[ord(ch)-ord_a]-=1
            chars.pop(k)          
            break
        match_count=0
        for j in range(26):
            c1=counts1[j]
            c2=counts2[j]
            if j==ord(ch)-ord_a:
                c2-=1
            match_count+=min(c1,c2)
        if (N-i-match_count)+fix_d<=K:
            T+=ch
            counts2[ord(ch)-ord_a]-=1
            chars.pop(k)
            fix_d+=1
            break
print(T)
