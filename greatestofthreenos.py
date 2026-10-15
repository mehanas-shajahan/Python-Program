#greatest of three nos
a=int(input())
b=int(input())
c=int(input())
if a>b:
    print("a is greater")
    if b>c:
        print("b is greater")
    else:
        print("c is greater")
elif a>c:
    print("a is greater")
else:
    print("c is greater")  