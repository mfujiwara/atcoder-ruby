N=int(input())
S=input()
for i,ch in enumerate(S):
    if ch=="1":
        if i%2==0:
            print("Takahashi")
            exit()
        else:
            print("Aoki")
            exit()
