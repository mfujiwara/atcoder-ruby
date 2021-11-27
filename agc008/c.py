I,O,T,J,L,S,Z=map(int, input().split())
if I%2==0 and J%2==0 and L%2==0:
    print(O+I+J+L)
elif I%2==0 and J%2==0 and L%2==1:
    print(O+I+J+L-1)
elif I%2==0 and J%2==1 and L%2==0:
    print(O+I+J+L-1)
elif I%2==0 and J%2==1 and L%2==1:
    if I==0:
        print(O+I+J+L-2)
    else:
        print(O+I+J+L-1)
elif I%2==1 and J%2==0 and L%2==0:
    print(O+I+J+L-1)
elif I%2==1 and J%2==0 and L%2==1:
    if J==0:
        print(O+I+J+L-2)
    else:
        print(O+I+J+L-1)
elif I%2==1 and J%2==1 and L%2==0:
    if L==0:
        print(O+I+J+L-2)
    else:
        print(O+I+J+L-1)
else:
    print(O+I+J+L)
