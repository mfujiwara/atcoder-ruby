import collections
T=int(input())
for _ in range(T):
    N=int(input())
    array=list(map(int, input().split()))
    counts=collections.defaultdict(int)
    for a in array:
        counts[a]+=1
    if N%2==0 and all([counts[c]%2==0 for c in counts]):
        print("Second")
    else:
        if N%2==0:
            print("First")
        else:
            print("Second")
