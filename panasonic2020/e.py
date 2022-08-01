a=[-1 if ch=="?" else ord(ch) for ch in input()]
b=[-1 if ch=="?" else ord(ch) for ch in input()]
c=[-1 if ch=="?" else ord(ch) for ch in input()]
maxi=max(len(a),len(b),len(c))

def calc(x,y):
    # xy[i]:=xの開始indexを0,yの開始indexをjにして重ねた時にokか
    xy={}
    for i in range(-maxi,maxi+1):
        v=True
        for j in range(len(x)):
            if 0<=j-i<len(y):
                if y[j-i]!=-1 and x[j]!=-1 and y[j-i]!=x[j]:
                    v=False
                    break
        xy[i]=v
    return xy
ab=calc(a,b)
ac=calc(a,c)
bc=calc(b,c)

ret=maxi*3
# aの開始indexを0,bの開始indexをi,cの開始indexをjにして重ねた時を調べる
for i in range(-maxi*2,maxi*2+1):
    for j in range(-maxi*2,maxi*2+1):
        v=True
        v&= i<=-maxi or maxi<=i or ab[i]
        v&= j<=-maxi or maxi<=j or ac[j]
        v&= -i+j<=-maxi or maxi<=-i+j or bc[-i+j]
        if v:
            ret=min(ret,max(len(a),i+len(b),j+len(c))-min(0, i, j))
print(ret)
