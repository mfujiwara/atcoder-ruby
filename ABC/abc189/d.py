N=int(input())
t_c=1
f_c=1
for i in range(N):
    s=input()
    if s=="AND":
        t_c,f_c = t_c, t_c+f_c*2
    else:
        t_c,f_c = t_c*2+f_c, f_c
print(t_c)
