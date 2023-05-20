A,B=map(int, input().split())
grid=[["#"]*100 for i in range(20)] + [["."]*100 for i in range(20)]
for i in range(A-1):
    row=i//50*2
    col=i%50*2
    grid[row][col]="."
for i in range(B-1):
    row=i//50*2
    col=i%50*2
    grid[39-row][99-col]="#"
print("40 100")
for g in grid:
    print("".join(g))
