def suffixArray(s):
    n = len(s)
    m = 30 # using Counting Sort when m is not too large, m is defined based on given data
 
    sa = [0] * (n + 1)
    rk = [0] * (2 * n + 1)
    tmp = [0] * (2 * n + 1)
    idx = [0] * (n + 1)
    px = [0] * (n + 1)
    cnt = [0] * (m + 1)
 
    for i in range(1, n + 1):
        # note: rk[i] >= 1
        rk[i] = ord(s[i - 1]) - ord('a') + 1 # for s is a string
        cnt[rk[i]] += 1
    for i in range(1, m + 1): cnt[i] += cnt[i - 1]
    for i in range(n, 0, -1):
        sa[cnt[rk[i]]] = i
        cnt[rk[i]] -= 1
 
    w = 1
    while True:
        p = 0
        for i in range(n, n - w, -1):
            p += 1
            idx[p] = i
        for i in range(1, n + 1):
            if sa[i] > w:
                p += 1
                idx[p] = sa[i] - w
        cnt = [0] * (m + 1) # memory could be saved here
        for i in range(1, n + 1):
            px[i] = rk[idx[i]]
            cnt[px[i]] += 1
        for i in range(1, m + 1): cnt[i] += cnt[i - 1]
        for i in range(n, 0, -1):
            sa[cnt[px[i]]] = idx[i]
            cnt[px[i]] -= 1
        for i in range(1, n + 1): tmp[i] = rk[i]
        p = 0
        for i in range(1, n + 1):
            if (tmp[sa[i]], tmp[sa[i] + w]) == (tmp[sa[i - 1]], tmp[sa[i - 1] + w]):
                rk[sa[i]] = p
            else:
                p += 1
                rk[sa[i]] = p
        if p == n:
            for i in range(1, n + 1): sa[rk[i]] = i
            break
        w <<= 1
        m = p
 
    # calculate height array
    ht = [0] * (n + 1)
    k = 0
    for i in range(1, n + 1):
        if k: k -= 1
        while i + k <= n and sa[rk[i] - 1] + k <= n and s[i + k - 1] == s[sa[rk[i] - 1] + k - 1]: k += 1
        ht[rk[i]] = k

    return sa[1:], ht[2:]    
N=int(input())
S=input()
s_array,h_array=suffixArray(S)
# print(s_array)
# print(h_array)

rets=[0]*N
# LCP Arrayの広義単調増加なindexを残していく
stack=[-1]
cur=0
for i in range(N-1):
    # s_array[i+1]-1から開始する文字列と、それより辞書順で小さいものの類似度を求める
    while len(stack)>1 and h_array[i]<h_array[stack[-1]]:
        # 新しいLCP Arrayの値が小さい場合はstackをpop
        j=stack.pop()
        cur-=h_array[j]*(j-stack[-1])
    cur+=h_array[i]*(i-stack[-1])
    stack.append(i)
    rets[s_array[i+1]-1]+=cur
# LCP Arrayの広義単調増加なindexを残していく
stack=[N-1]
cur=0
for i in range(N-2,-1,-1):
    # s_array[i]-1から開始する文字列と、それより辞書順で大きいものの類似度を求める
    while len(stack)>1 and h_array[i]<h_array[stack[-1]]:
        # 新しいLCP Arrayの値が小さい場合はstackをpop
        j=stack.pop()
        cur-=h_array[j]*(stack[-1]-j)
    cur+=h_array[i]*(stack[-1]-i)
    stack.append(i)
    rets[s_array[i]-1]+=cur

# 同じ文字列同士のケースを足す
for i in range(N):
    rets[i]+=N-i
for ret in rets:
    print(ret)
