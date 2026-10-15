num=int(input())
digits=0
temp=num
temp1=num
while num!=0:
    digits+=1
    num//=10
sums=0
while temp!=0:
    rem=temp%10
    sums=sums+rem**digits
    temp=temp//10
if temp1==sums:
    print("Amstrong number")
else:
    print("Not an Amstrong number")