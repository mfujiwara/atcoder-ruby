C=[list(map(int, input().split())) for _ in range(3)]
for i in range(2):
    d1=C[0][i]-C[0][i+1]
    d2=C[1][i]-C[1][i+1]
    d3=C[2][i]-C[2][i+1]
    if d1!=d2 or d2!=d3:
        print("No")
        exit()
for i in range(2):
    d1=C[i][0]-C[i+1][0]
    d2=C[i][1]-C[i+1][1]
    d3=C[i][2]-C[i+1][2]
    if d1!=d2 or d2!=d3:
        print("No")
        exit()
print("Yes")
