# #list ordered mutable allow duplicate    
list_1=[24,56,78,9,23,23]
list_2=["Jagan","Kumar","Navin","Praveen"]
list_3=["Naveen",18,"M","RGCET",True]
print(list_1)
print(list_2)
print(list_3)
print(type(list_1))
list_4=[10,20,30,40]
list_4[2]=300
print(list_4)

numbers=[]
n=int(input())
for i in range(n):
    data=int(input())
    numbers.append(data)
print(numbers)

list_5=[1,2,3,4,5]
print(list_5)

for data in list_5:
    print(data,end=" ")
print()
i=0
while i<len(list_5):
    print(list_5[i],end=" ")
    i+=1
print()
list_6=[1,2,3,4,5]
list_6.append(6)
list_6.append(7)
print(list_6)
list_6.insert(0,1000)
print(list_6)

list_7=[10,20,30,40,20,30]
list_7.remove(30)
print(list_7)
list_7.pop()
print(list_7)
list_7.clear()
print(list_7)

print("Index")
list_7=[10,20,30,40,20,30]
print(list_7[4])
print(list_7[-4])