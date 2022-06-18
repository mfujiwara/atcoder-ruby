h1,h2,h3,w1,w2,w3=map(int, input().split())
ret=0
for a in range(1,29):
    for b in range(1,29):
        for c in range(1,29):
            for d in range(1,29):
                ab=h1-a-b
                if ab<=0:
                    continue
                cd=h2-c-d
                if cd<=0:
                    continue
                x=w3-ab-cd
                if x<=0:
                    continue
                ac=w1-a-c
                if ac<=0:
                    continue
                bd=w2-b-d
                if bd<=0:
                    continue
                y=h3-ac-bd
                if y<=0:
                    continue
                if x==y:
                    ret+=1
print(ret)
