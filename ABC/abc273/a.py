N=int(input())
def calc(k):
    if k==0: return 1
    return calc(k-1)*k
print(calc(N))
