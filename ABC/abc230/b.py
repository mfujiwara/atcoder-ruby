S=input()
T1="oxxoxxoxxoxxoxx"[:len(S)]
T2="xxoxxoxxoxxoxxo"[:len(S)]
T3="xoxxoxxoxxoxxox"[:len(S)]
if S in [T1,T2,T3]:
    print("Yes")
else:
    print("No")
