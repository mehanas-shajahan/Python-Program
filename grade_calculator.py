#grade calculator
mark=int(input("Enter the mark: "))
if mark in range(90,100):
    print("A")
elif mark in range(75,89):
    print("B")
elif mark in range(60,74):
    print("C")
elif mark in range(40,59):
    print("D")
else:
    print("Fail")    