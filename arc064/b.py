s=input()
if (s[0]==s[-1]) ^ (len(s)%2==0):
    print("Second")
else:
    print("First")
