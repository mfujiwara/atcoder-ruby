T=int(input())
for _ in range(T):
    S=input()
    if S>"atcoder":
        print(0)
    elif S.count("a")==len(S):
        print(-1)
    else:
        for i,ch in enumerate(S):
            if ch!="a":
                if ch>"t":
                    print(i-1)
                else:
                    print(i)
                break
