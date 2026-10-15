

#two sum
nums=[]
n=int(input())
for i in range(n):
    data=int(input())
    nums.append(data)
target=int(input())
found=False
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            print(f"{i} , {j}")
            found=True
            break
    if found:
        break
if not found:
    print(-1,-1)

# #tuple ordered immutable allow duplicate
# tuple_1=(34,67,89,23)
# print(tuple_1)
# print(type(tuple_1))

# tuple_2=(5)
# print(type(tuple_2))

# tuple_3=(12,45,67,89,23)
# for data in tuple_3:
#     print(data,end=" ")
# print()
# i=0
# while i<len(tuple_3):
#     print(tuple_3[i],end=" ")
#     i+=1
# print()
# tuple_4=(1,2,3,2,3,1)
# print(tuple_4.count(3))
# print(tuple_4.index(3))
# print(len(tuple_4))
# print(sum(tuple_4))
# print(min(tuple_4))
# print(max(tuple_4))

# t=(10,20,10,30,20,40)
# for i in t:
#     if t.count(i)>1:
#         print(i)
#         t=tuple(x for x in t if x!=i)

# #set-unique unorderd mutable
# numbers={1,2,3,6,4,3,2}
# print(numbers)
# names={"Abinaya","Basha","david","Elango"}
# print(names)
# empty_set=set()
# empty_set={45,67,89}
# print(empty_set)

# nums1={10,20,30,40}
# print(nums1)
# nums1.add(50)
# print(nums1)
# nums1.update([60,70,80])
# print(nums1)

# nums2=[1,2,3,1,2,3,3,2,4,67,567]
# unique_set=set(nums2)
# print(unique_set)

# nums3={56,78,90,34,12}
# nums3.remove(56)
# print(nums3)
# nums3.discard(12)
# print(nums3)
# #nums3.remove(100)
# #print(nums3)
# nums3.discard(100)
# print(nums3)
# nums3.clear()
# print(nums3)

# nums4={1,2,3,4,5,6,7,8,9}
# for value in nums4:
#     print(value,end=" ")
# print()
# a={1,2,3,3}
# b={3,4,5}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# #mutable collection of key value pairs key unique values repeat
# student1={
#     "name":"mehu",
#     "age": 21,
#     "mark": 91,
#     "dept": "ece"
# }
# print(student1)
# print(student1["name"])
# print(student1["age"])
# print(student1.get("mark"))
# print(student1.get("city","Not Applicable"))
# student1["mark"]=450
# print(student1)
# student1["city"]="pondy"
# student1.pop("age")
# print(student1)
# print(student1)

# for a,b in student1.items():
#     print(a," :",b)

# #strings-collection of characters and immutable
# name="mehu"
# dept='python'
# print(name)
# print(dept)
# print(dept[0])
# print(dept[1])
# print(dept[-1])
# #pyt
# print(dept[:3])
# #thon
# print(dept[2:6])
# #pyth
# print(dept[0:4])
# #nohtyp
# print(dept[::-1])

# a="Python"#1000
# a="J"+a[1:]
# print(a)
# print(len(a))
# for ch in a:
#     print(ch,end=" ")
# print()
# text="Java Programming"
# print(text.upper())
# print(text.lower())
# print(text.replace("Java","Python"))
# print(text.count('a'))
# print(text.find("C"))
# print(text.startswith("Java"))
# print(text.endswith("Programming"))

# text1="            Java Programming            "
# print(text1.strip())
# text2="java python nodejs"
# courses=text2.split()
# print(courses)

# text3=["Python","Java","C++"]
# text4=",".join(text3)
# print(text4)

# def greet():  #function def
#     print("hi mehu")
# greet() #function calling
# greet()

# def addition(a,b):
#     print(a+b)

# addition(5,6)
# addition(100,200)
# addition(200,300)

# def multiplication(a,b,c):
#     return a*b*c

# result=multiplication(5,5,5)
# print(result)

# def college():
#     text="message" #local variable
#     print(text)
# college()

# message="hello"
# def google():
#     print(message)
# google(message)
# print(message)

# #recursion-fuction calling itself
# def greet(n):
#     if n==0:
#         return
#     print("Hello Mehu")
#     greet(n-1)
# greet(5)

# def counts(num):
#     if num==11:
#         return
#     print(num,end=" ")
#     counts(num+1)
# counts(1)
# print()
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# n=int(input())
# result=factorial(n)
# print(result)

# a=0
# b=1
# print(a," ",b,end=" ")
# for i in range(3,11):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
# print()
# def fib(num):
#     if num==0 or num==1:
#         return num
#     return fib(num-1)+fib(num-2)    

# num=int(input())
# print(fib(num))

# #lambda function
# #lambda arguements:expression
# import math
# from math import sqrt
# import Calculator
# addition=lambda a,b:a+b
# print(addition(4,3))
# square=lambda a:a*a 
# print(square(5))

# #modules and packages
# print(math.sqrt(25))
# print(math.factorial(25))
# print(math.pi)

# print(Calculator.multi(5,5,5))

# #Exception Handling 
# try:
#     a=int(input())
#     b=int(input())
#     c=a//b
#     print(c)
# except ZeroDivisionError:
#     print("Please Enter Positive Number: ")
# except ValueError:
#     print("Enter Integer Only: ")
# finally:
#     print("Java Programming ")

#oops-Object oriented programming language or system
#class object inheritance polymorphism encapsulation abstraction interface
# class studenttwo:
#     name="unknown"
#     mark=0
#     def display(self):
#         print(self.name," ",self.mark)

# class studentone:
#     name="mehu"
#     age=20
#     dept="ece"
#     def marks(self):
#         print("Maths: 90,English: 78")

# class studentthree:
#     name="unknown"
#     mark=0
#     def _init_(self,name,mark):
#         self.name=name
#         self.mark=mark

#     #def setdetails(self,name,mark):
#     #     self.name=name
#     #     self.mark=mark
#     def printdetails(self):
#         print(self.name," ",self.mark)

# s1=studentone()
# print(s1.name)
# print(s1.age)
# s1.marks

# s2=studenttwo()
# s2.name="aravind"
# s2.mark=345
# s2.display()
# s3=studenttwo()
# s3.name="dharshan"
# s3.mark=456
# s3.display()

# s4=studentthree("kumar",34)
# #s4.seddetails("jagan",500)
# s4.printdetails()

# #single inheritance -> one parent class one child class
# class Device:
#     def power_on(self):
#         print("Device Switched On")
#     class Phone(Device):
#         def call(self):
#             print("Making a phone call")
# samsung=Phone()
# samsung=power_on()
# samsung.call()
# print()
# #multilevel inheritance->Grandparent->son
# class Device:
#     def power_on(self):
#         print("Device switched on")
# class Laptop(Computer):
#     def charge(self):
#         print("Laptop battery charging")
# asus=Laptop()
# asus.power_on()
# asus.charge()
# print()
# #multiple inheritance one child class multiple parent class
# class Camera:
#     def take_photo(self):
#         print("Taking a photo")
# class MusicPlayer:
#     def play_music(self):
#         print("Playing Music")
# class SmartPhone(Camera,MusicPayer):
#     def call(self):
#         print("Making a phone call")
# mi=SmatPhone()
# mi.take_photo()
# mi.play_music()

#hierarchical inheritance-one parent class multiple child class
# class Device:
#     def power_on(self):
#         print("Device Switched On")
# class Phone(Device):
#     def call(self):
#         print("making a phone call")
# class Computer(Device):
#     def run_program(self):
#         print("running a python program")
# samsung=Phone()
# samsung.call()
# samsung.power_on()
# hp=Computer()
# hp.power_on()
# hp.run_program()
# #hybrid inheritance-more than one inheritance in a single program

# #polymorphism
# class phone:
#     def camera (self):
#         print("taking a normal photo")
# class smartphone(phone):
#     def camera(self):
#         print("taking a portrait photo")
# samsung=smartphone()
# samsung.camera()
# nokia=phone()
# nokia.camera()
#encapsulation
# class bank:
#     __amount=800
#     def printamount(self):
#         return self.__amount
#     hdfc=bank()
#     print(hdfc.printaamount())
#     #abstraction
#     from abc import ABC,abstractmethod
#     class payment(ABC):
#         @abstractmethod
#         def pay(self):
#             pass
#     class UPI (payment):
#         def pay (self):
#             print("payment done using phonepe")
#     payment=UPI()
#     payment.pay()
#     payment=UPI()
#     payment.pay()

         



    
    




















    
    
    

    



