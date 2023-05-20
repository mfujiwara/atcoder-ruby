N=int(input())
array=list(map(int, input().split()))
dp=1
S=0
for a in array:
    dp|=dp<<a # bitwise OR
    S+=a
dp>>=(S+1)//2 # 分岐点より大きいものに絞る
# 分岐点の数にdpの最下位bitまで長さを足せば答え
ans=(dp&-dp).bit_length()+(S+1)//2-1
print(ans)
