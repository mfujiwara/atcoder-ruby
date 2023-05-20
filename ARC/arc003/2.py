N=int(input())
words=[]
for _ in range(N):
    s=input()
    words.append(s[::-1])
words.sort()
for w in words:
    print(w[::-1])
