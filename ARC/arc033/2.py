Na,Nb=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
a_set=set(a_array)
b_set=set(b_array)
ab_set1=a_set&b_set
ab_set2=a_set|b_set
print(len(ab_set1)/len(ab_set2))
