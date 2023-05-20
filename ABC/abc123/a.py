abcde=[]
for _ in range(5):
    abcde.append(int(input()))
k=int(input())
if abcde[0]+k<abcde[-1]:
    print(":(")
else:
    print("Yay!")
