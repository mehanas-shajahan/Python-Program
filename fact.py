num=int(input("Enter number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
    print(i,end=" ")
    if i<num:
        print("*",end=" ")
print("=",fact)
