import collections
N=int(input())
counts=collections.defaultdict(int)
for _ in range(N):
    S=input()
    counts[S]+=1
for key in ["AC","WA","TLE", "RE"]:
    print(key + " x " + str(counts[key]))
