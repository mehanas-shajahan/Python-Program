#matchcase op
num1=int(input("Enter first no: "))
num2=int(input("Enter first no: "))
operator=input("Enter Operator: ")
match operator:
    case '+':print(num1+num2)
    case '-':print(num1-num2)
    case '*':print(num1*num2)
    case '/':print(num1/num2)
    case '//':print(num1//num2)
    case '%':print(num1%num2)
    case '**':print(num1**num2)