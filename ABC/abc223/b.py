S=input()
mini=S
maxi=S
for i in range(len(S)):
    S=S[1:]+S[:1]
    mini=min(mini,S)
    maxi=max(maxi,S)
print(mini)
print(maxi)
