import itertools
N=int(input())
for prod in itertools.product("abc",repeat=N):
    print("".join(list(prod)))
