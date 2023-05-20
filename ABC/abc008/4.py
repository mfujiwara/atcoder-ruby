from functools import lru_cache
@lru_cache(maxsize=None)
def calc(hi,hj,wi,wj):
  if hi>hj or wi>wj:
    return 0
  ret=0
  dh,dw=hj-hi+1,wj-wi+1
  for x,y in xy:
    if hi<=x<=hj and wi<=y<=wj:
      tmp=calc(hi,x-1,wi,y-1)+calc(x+1,hj,wi,y-1)+calc(hi,x-1,y+1,wj)+calc(x+1,hj,y+1,wj)+dh+dw-1
      ret=max(ret,tmp)
  return ret
W,H=map(int,input().split())
N=int(input())
xy=[]
for i in range(N):
  x,y=map(int,input().split())
  xy.append((x,y))
print(calc(1,W,1,H))
