H,W,N=map(int, input().split())
rows=set()
cols=set()
abs=[]
for _ in range(N):
    a,b=map(int, input().split())
    abs.append((a,b))
    rows.add(a)
    cols.add(b)
rows=sorted(list(rows))
cols=sorted(list(cols))
new_rows={}
new_cols={}
for i,r in enumerate(rows):
    new_rows[r]=i+1
for i,c in enumerate(cols):
    new_cols[c]=i+1
for a,b in abs:
    print(f"{new_rows[a]} {new_cols[b]}")
