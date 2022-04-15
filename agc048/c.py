import collections
N,L=map(int, input().split())
a_array=[0]+list(map(int, input().split()))+[L+1]
b_array=[0]+list(map(int, input().split()))+[L+1]
x_array=[a_array[i]-i for i in range(N+2)] # 開始点の左の空きマスの数
y_array=[b_array[i]-i for i in range(N+2)] # 終了点の左の空きマスの数
ret=0
memo=[0]*(N+2)
x2i={} # xのindex
# 左に動かす
for i in range(N+1):
    x2i[x_array[i]]=i
    if y_array[i]!=y_array[i+1]: # くっつくものはまとめて考える
        if y_array[i] in x2i:
            ret+=max(i-x2i[y_array[i]],0)
        else:
            memo[i]+=1
x2i={}
# 右に動かす
for i in range(N+1)[::-1]:    
    x2i[x_array[i+1]]=i+1
    if y_array[i]!=y_array[i+1]: # くっつくものはまとめて考える
        if y_array[i+1] in x2i:
            ret+=max(x2i[y_array[i+1]]-(i+1),0)
        else:
            memo[i+1]+=1
if max(memo)==2:
    # 左右どちらでも不可のものがあった
    print(-1)
else:
    print(ret)
