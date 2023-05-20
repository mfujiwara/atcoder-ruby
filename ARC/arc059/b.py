import sys
from collections import defaultdict
s=input()
pre_positions=defaultdict(lambda: -1)
for i,ch in enumerate(s):
    pre=pre_positions[ch]
    if pre==-1 or pre+2<i:
        pre_positions[ch]=i
    else:
        print("{} {}".format(pre+1, i+1))
        sys.exit()
print("-1 -1")
