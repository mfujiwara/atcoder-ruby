MOD=10**9+7
N=int(input())
S=input()
memo=[0]*7 #atcoder
for ch in S:
    if ch=="a":
        memo[0]+=1
    elif ch=="t":
        memo[1]+=memo[0]
    elif ch=="c":
        memo[2]+=memo[1]
    elif ch=="o":
        memo[3]+=memo[2]
    elif ch=="d":
        memo[4]+=memo[3]
    elif ch=="e":
        memo[5]+=memo[4]
    elif ch=="r":
        memo[6]+=memo[5]
print(memo[-1]%MOD)
