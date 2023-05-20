import collections
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
N,K=map(int, input().split())
S=list(map(ord,list(input())))
divisors=make_divisors(N)
for div in divisors[::-1]:
    def check():
        must=0
        for j in range(N//div):
            counts=collections.defaultdict(int)
            for i in range(div):
                #print("index",i+N//div*j)
                a=S[j+N//div*i]
                counts[a]+=1
            c,_=max([(c,a) for a,c in counts.items()])
            #print("c",c)
            must+=div-c
        #print(must)
        return must<=K
    if check():
        print(N//div)
        break
