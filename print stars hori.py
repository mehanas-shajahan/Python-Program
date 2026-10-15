n=int(input())
a=n+1
b=5
for i in range(1,n*2):
    for j in range(0,a-1):
        print(" ",end=" ")
    for j in range(1,b+1):
        print("*",end=" ")
    print()
    if i>=5:
            a-=1
            b+=1
    else:
            a+=1
            b-=1