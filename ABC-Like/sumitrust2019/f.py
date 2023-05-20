t1,t2=map(int, input().split())
a1,a2=map(int, input().split())
b1,b2=map(int, input().split())
takahashi1=a1*t1+a2*t2
aoki1=b1*t1+b2*t2
if takahashi1==aoki1:
    print("infinity")
elif a1>b1 and takahashi1>aoki1 or a1<b1 and takahashi1<aoki1:
    print(0)
else:
    diff=abs(takahashi1-aoki1)
    diff2=abs(b2*t2-a2*t2)
    n=diff2//diff
    if diff*n==diff2:
        print(2*n-2)
    else:
        print(2*n-1)
