#discount
amount=float(input("Enter Purchase Amount"))
if amount<0:
    print("Invalid Result")
else:
    discount=0.0
    if amount>=5000:
        discount=amount*20/100
    elif amount>=2000 and amount<5000:
        discount=amount*10/100
    print("Discount amount: ",discount)
    print("Final Payable Amount: ",amount-discount)