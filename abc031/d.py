K,N=map(int, input().split())
words=[]
for _ in range(N):
    v,w=input().split()
    words.append((v,w))
def calc(goro, words):
    if len(words)==0:
        return True
    v,w=words.pop()
    if len(v)==0:
        words.append((v,w))
        return False
    if v[0] in goro:
        v_g=goro[v[0]]
        if v_g==w:
            if calc(goro,words):
                return True
            else:
                words.append((v,w))
                return False
        if len(v_g)>len(w) or v_g!=w[:len(v_g)]:
            words.append((v,w))
            return False
        else:
            next_v=v[1:]
            next_w=w[len(v_g):]
            words.append((next_v,next_w))
            if calc(goro,words):
                return True
            else:
                words.pop()
                words.append((v,w))
                return False
    else:
        words.append((v,w))
        for i in range(min(3,len(w))):
            v_g=w[:i+1]
            goro[v[0]]=v_g
            if calc(goro,words):
                return True
            else:
                goro.pop(v[0])
        return False
ggg={}
calc(ggg,words)
for i in range(1,K+1):
    print(ggg[str(i)])
