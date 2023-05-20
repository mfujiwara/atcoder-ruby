import itertools
S,K=input().split()
K=int(K)
dic=set(itertools.permutations(S,len(S)))
dic=sorted(list(dic))
print("".join(dic[K-1]))
