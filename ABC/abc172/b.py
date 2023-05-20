S=input()
T=input()
print(sum([0 if S[i]==T[i] else 1 for i in range(len(S))]))
