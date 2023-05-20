N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
ret=0
# 下位bitから求めていく
for i in range(30):
    t=pow(2,i)
    # 不要な部分はmodで削る
    aaa=[a%(2*t) for a in a_array]
    bbb=[b%(2*t) for b in b_array]
    aaa.sort()
    bbb.sort()
    # aaa,bbbのx以下になる組み合わせの数を尺取法を使って求める
    def calc(x):
        ret=0
        p=len(bbb)-1
        for i in range(len(aaa)):
            while p>=0 and aaa[i]+bbb[p]>x:
                p-=1
            ret+=p+1
        return ret
    count=0
    # 0..2*(2^i-1) の値があり得るのでその中からiビット目が1になるものをカウント
    count+=calc(2*t-1)-calc(t-1)
    count+=calc(4*t-1)-calc(3*t-1)
    if count%2==1:
        ret+=t
print(ret)
