deg,dis=map(int, input().split())
if dis<15:
    dir="C"
elif deg<112.5:
    dir="N"
elif deg<337.5:
    dir="NNE"
elif deg<562.5:
    dir="NE"
elif deg<787.5:
    dir="ENE"
elif deg<1012.5:
    dir="E"
elif deg<1237.5:
    dir="ESE"
elif deg<1462.5:
    dir="SE"
elif deg<1687.5:
    dir="SSE"
elif deg<1912.5:
    dir="S"
elif deg<2137.5:
    dir="SSW"
elif deg<2362.5:
    dir="SW"
elif deg<2587.5:
    dir="WSW"
elif deg<2812.5:
    dir="W"
elif deg<3037.5:
    dir="WNW"
elif deg<3262.5:
    dir="NW"
elif deg<3487.5:
    dir="NNW"
else:
    dir="N"
if dis<15:
    w=0
elif dis<93:
    w=1
elif dis<201:
    w=2
elif dis<327:
    w=3
elif dis<477:
    w=4
elif dis<645:
    w=5
elif dis<831:
    w=6
elif dis<1029:
    w=7
elif dis<1245:
    w=8
elif dis<1467:
    w=9
elif dis<1707:
    w=10
elif dis<1959:
    w=11
else:
    w=12
print(dir,w)
