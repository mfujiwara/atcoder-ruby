import itertools
H1,W1=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(H1)]
H2,W2=map(int, input().split())
B=[list(map(int, input().split())) for _ in range(H2)]
def calc(h_comb,w_comb):
    for i,h in enumerate(h_comb):
        for j,w in enumerate(w_comb):
            if A[h][w]!=B[i][j]:
                return False
    return True
for h_comb in itertools.combinations(range(H1),H2):
    for w_comb in itertools.combinations(range(W1),W2):
        if calc(h_comb,w_comb):
            print("Yes")
            exit()
print("No")
