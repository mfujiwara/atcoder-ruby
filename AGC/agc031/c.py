N,A,B=map(int, input().split())
a=A
b=B
diffs=[]
i=0
while a!=0 or b!=0:
    a,a0=divmod(a,2)
    b,b0=divmod(b,2)
    if a0!=b0:
        diffs.append(i)
    i+=1
#print(diffs)
if len(diffs)%2==0:
    print("NO")
    exit()
diffs0=diffs[:len(diffs)//2+1]
diffs1=diffs[len(diffs)//2+1:]
#print(diffs,diffs0,diffs1)
codes=[]
# 方針決定
targets=[]
end=B
for i in range(len(diffs0)):
    d0=diffs0.pop()
    start=end^pow(2,d0)
    if len(diffs0)==0:
        targets.append((start,end,N-i,diffs1))
    else:
        targets.append((start,end,N-i-1,diffs1[:i+1]))
    if i<len(diffs1):
        end=start^pow(2,diffs1[i])
# print("targets",targets)
rets=[]
while targets:
    start,end,n,skipBit=targets.pop()
    # ベースになるグレイコードを生成
    codes=[]
    for k in range(pow(2,n)):
        codes.append(k ^ (k >> 1))
    # print(codes)
    # skipBitのbitはスキップする
    for i in range(len(codes)):
        for d in skipBit:
            a=codes[i]&(pow(2,d)-1)
            b=codes[i]//pow(2,d)*pow(2,d+1)
            codes[i]=(a+b)
    # print(codes)
    # diffs0のbitで差分が出るようにする
    b0=start^end
    b1=codes[-1]
    if b0!=b1:
        for i in range(len(codes)):
            if b0&codes[i]>0 and b1&codes[i]==0:
                codes[i]^=b0
                codes[i]|=b1
            elif b0&codes[i]==0 and b1&codes[i]>0:
                codes[i]|=b0
                codes[i]^=b1
            codes[i]^=start
    else:
        for i in range(len(codes)):
            codes[i]^=start
    # print(codes)
    # skipBitで飛ばすbitをstart,endに合わせる
    for i in range(len(codes)):
        for d in skipBit:
            if pow(2,d)&end>0:
                codes[i]|=pow(2,d)
    # print(codes)
    rets+=codes
print("YES")
print(*rets)
