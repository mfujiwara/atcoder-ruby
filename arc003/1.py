N=int(input())
R=input()
def calc(ch):
    if ch=="A":
        return 4
    elif ch=="B":
        return 3
    elif ch=="C":
        return 2
    elif ch=="D":
        return 1
    else:
        return 0
print(sum(list(map(calc,list(R))))/N)
