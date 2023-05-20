array=list(map(int, input().split()))
s=[]
base=ord("a")-1
for a in array:
    s.append(chr(a+base))
print("".join(s))
