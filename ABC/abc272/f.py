import collections
def sais(s: str):
    uniq = list(set(s))
    uniq.sort()
    return sais_rec(list(map({e: i + 1 for i, e in enumerate(uniq)}.__getitem__, s)), len(uniq))
def sais_rec(lst, num):
    L = len(lst)
    if L < 2:
        return lst + [0]
    lst = lst + [0]
    L += 1
    res = [-1] * L
    t = [1] * L
    for i in range(L - 2, -1, -1):
        t[i] = 1 if (lst[i] < lst[i + 1] or (lst[i] == lst[i + 1] and t[i + 1])) else 0
    isLMS = [t[i - 1] < t[i] for i in range(L)]
    LMS = [i for i in range(1, L) if t[i - 1] < t[i]]
    LMSn = len(LMS)

    count = collections.Counter(lst)
    tmp = 0
    cstart = [0] * (num + 1)
    cend = [0] * (num + 1)
    for key in range(num + 1):
        cstart[key] = tmp
        cend[key] = tmp = tmp + count[key]

    cc_it = [iter(range(e - 1, s - 1, -1)) for s, e in zip(cstart, cend)]
    for e in reversed(LMS):
        res[next(cc_it[lst[e]])] = e

    cs_it = [iter(range(s, e)) for s, e in zip(cstart, cend)]
    ce_it = [iter(range(e - 1, s - 1, -1)) for s, e in zip(cstart, cend)]
    for e in res:
        if e > 0 and not t[e - 1]:
            res[next(cs_it[lst[e - 1]])] = e - 1
    for e in reversed(res):
        if e > 0 and t[e - 1]:
            res[next(ce_it[lst[e - 1]])] = e - 1

    name = 0
    prev = -1
    pLMS = {}
    for e in res:
        if isLMS[e]:
            if prev == -1 or lst[e] != lst[prev]:
                name += 1
                prev = e
            else:
                for i in range(1, L):
                    if lst[e + i] != lst[prev + i]:
                        name += 1
                        prev = e
                        break
                    if isLMS[e + i] or isLMS[prev + i]:
                        break
            pLMS[e] = name - 1

    if name < LMSn:
        sublst = [pLMS[e] for e in LMS if e < L - 1]
        ret = sais_rec(sublst, name - 1)

        LMS = list(map(LMS.__getitem__, reversed(ret)))
    else:
        LMS = [e for e in reversed(res) if isLMS[e]]

    res = [-1] * L

    cc_it = [iter(range(e - 1, s - 1, -1)) for s, e in zip(cstart, cend)]
    for e in LMS:
        res[next(cc_it[lst[e]])] = e

    cs_it = [iter(range(s, e)) for s, e in zip(cstart, cend)]
    ce_it = [iter(range(e - 1, s - 1, -1)) for s, e in zip(cstart, cend)]

    for e in res:
        if e > 0 and not t[e - 1]:
            res[next(cs_it[lst[e - 1]])] = e - 1
    for e in reversed(res):
        if e > 0 and t[e - 1]:
            res[next(ce_it[lst[e - 1]])] = e - 1
    return res
N=int(input())
S=input()
T=input()
suffix_array=sais(S*2+"a"*N+T*2+"z"*N)
ret=0
count=0
for s in suffix_array:
    if 0<=s<N:
        # 1個目のSのindex
        count+=1
    if N*3<=s<N*4:
        # 1個目のTのindex
        ret+=count
print(ret)
