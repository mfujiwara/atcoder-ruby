import itertools
N=int(input())
p_array=tuple(map(int, input().split()))
q_array=tuple(map(int, input().split()))
perm=sorted(list(itertools.permutations([i+1 for i in range(N)])))
print(abs(perm.index(p_array)-perm.index(q_array)))
