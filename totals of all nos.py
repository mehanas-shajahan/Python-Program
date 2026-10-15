num1=int(input("Enter Fnumber: "))
num2=int(input("Enter Snumber: "))
totals=0
for i in range(num1,num2+1):
    if i%2==0:
        totals+=i
print(totals)