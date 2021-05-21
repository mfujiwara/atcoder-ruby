MOD=10**9+7
n,m=map(int, input().split())
x_array=list(map(int, input().split()))
y_array=list(map(int, input().split()))
x=0
for i in range(n-1):
    x+=(x_array[i+1]-x_array[i])*(i+1)*(n-1-i)
    x%=MOD
y=0
for i in range(m-1):
    y+=(y_array[i+1]-y_array[i])*(i+1)*(m-1-i)
    y%=MOD
print(x*y%MOD)
