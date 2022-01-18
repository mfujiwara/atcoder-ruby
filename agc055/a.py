N=int(input())
S=input()
S=[0 if ch=="A" else 1 if ch=="B" else 2 for ch in S]
counts=[[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(N):
        counts[i][S[i*N+j]]+=1
p1=min(counts[0][0],counts[1][1],counts[2][2]) #ABC
counts[0][0]-=p1
counts[1][1]-=p1
counts[2][2]-=p1
p2=min(counts[0][0],counts[1][2],counts[2][1]) #ACB
counts[0][0]-=p2
counts[1][2]-=p2
counts[2][1]-=p2
p3=min(counts[0][1],counts[1][0],counts[2][2]) #BAC
counts[0][1]-=p3
counts[1][0]-=p3
counts[2][2]-=p3
p4=min(counts[0][1],counts[1][2],counts[2][0]) #BCA
counts[0][1]-=p4
counts[1][2]-=p4
counts[2][0]-=p4
p5=min(counts[0][2],counts[1][0],counts[2][1]) #CAB
counts[0][2]-=p5
counts[1][0]-=p5
counts[2][1]-=p5
p6=min(counts[0][2],counts[1][1],counts[2][0]) #CBA
counts[0][2]-=p6
counts[1][1]-=p6
counts[2][0]-=p6
rets=[]
for i in range(3):
    q1=q2=q3=q4=q5=q6=0
    for j in range(N):
        if S[i*N+j]==0:
            if i==0:
                if q1<p1:
                    q1+=1
                    rets.append(1)
                else:
                    rets.append(2)
            elif i==1:
                if q3<p3:
                    q3+=1
                    rets.append(3)
                else:
                    rets.append(5)
            else:
                if q4<p4:
                    q4+=1
                    rets.append(4)
                else:
                    rets.append(6)
        elif S[i*N+j]==1:
            if i==0:
                if q3<p3:
                    q3+=1
                    rets.append(3)
                else:
                    rets.append(4)
            elif i==1:
                if q1<p1:
                    q1+=1
                    rets.append(1)
                else:
                    rets.append(6)
            else:
                if q2<p2:
                    q2+=1
                    rets.append(2)
                else:
                    rets.append(5)
        else:
            if i==0:
                if q5<p5:
                    q5+=1
                    rets.append(5)
                else:
                    rets.append(6)
            elif i==1:
                if q2<p2:
                    q2+=1
                    rets.append(2)
                else:
                    rets.append(4)
            else:
                if q1<p1:
                    q1+=1
                    rets.append(1)
                else:
                    rets.append(3)
print("".join(map(str,rets)))
