n=int(input())
digits=0
total=0
while n!=0:
    rem=n%10
    digits+=1
    total=total+rem
    n=n//10
print("No of digits: ",digits)
print("Sum of digits: ",total)