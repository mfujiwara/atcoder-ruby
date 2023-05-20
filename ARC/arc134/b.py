import collections
N=int(input())
s=list(input())
counts=collections.defaultdict(int)
for ch in s:
    counts[ch]+=1
keys=list(sorted(list(counts.keys())))
end_i=N-1
for i in range(N):
    if i>=end_i:
        break
    ch=s[i]
    if ch==keys[0]:
        counts[ch]-=1
        if counts[ch]==0:
            keys.remove(ch)
    else:
        while s[end_i]!=keys[0]:
            counts[s[end_i]]-=1
            if counts[s[end_i]]==0:
                keys.remove(s[end_i])
            end_i-=1
        s[i],s[end_i]=s[end_i],s[i]
        counts[ch]-=1
        counts[keys[0]]-=1
        if counts[ch]==0:
            keys.remove(ch)
        if counts[keys[0]]==0:
            keys.remove(keys[0])
        end_i-=1
print("".join(s))
