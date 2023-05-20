import datetime
Y,M,D=map(int,input().split("/"))
d=datetime.datetime(Y, M, D)
while d.year%(d.month*d.day)!=0:
    d+= datetime.timedelta(days=1)
print(d.strftime('%Y/%m/%d'))
