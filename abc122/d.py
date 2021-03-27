import sys
from collections import defaultdict
MOD=10**9+7
N=int(input())
if N==3:
    print(61)
    sys.exit()
dic=defaultdict(int)
for i in ["A","C","G","T"]:
    for j in ["A","C","G","T"]:
        for k in ["A","C","G","T"]:
            s=i+j+k
            if s!="AGC" and s!="ACG" and s!="GAC":
                dic[s]=1
for i in range(4,N+1):
    next_dic=defaultdict(int)
    for s in dic:
        t=(s+"A")[1:]
        next_dic[t]+=dic[s]
        next_dic[t]%=MOD
        if s[0:2]!="AG" and s[1:3]!="AG" and s[1:3]!="GA" and s!="AGG" and s!="ATG":
            t=(s+"C")[1:]
            next_dic[t]+=dic[s]
            next_dic[t]%=MOD
        if s[1:3]!="AC":
            t=(s+"G")[1:]
            next_dic[t]+=dic[s]
            next_dic[t]%=MOD
        t=(s+"T")[1:]
        next_dic[t]+=dic[s]
        next_dic[t]%=MOD
    dic=next_dic
r=0
for v in dic.values():
    r+=v
    r%=MOD
print(r)
