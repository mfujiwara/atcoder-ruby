N=int(input())
# 2 3 5 7
# 84 60 105 70 
#array=[30,42,70,105]
array=["6", "10", "15"]
if N>3:
    for i in range(16,10001):
        if i%6==0 or i%10==0 or i%15==0:
            array.append(str(i))
            if len(array)==N: break
print(" ".join(array))
