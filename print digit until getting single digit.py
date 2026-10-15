num=int(input())
while not (num>=0 and num<=9):
    sums=0
    while num!=0:
        rem=num%10
        sums=sums+rem
        num=num//10
    num=sums
else:
    print(num)