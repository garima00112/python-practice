#This is the python program which find 3 greatest number.


a= input("Enter 1st number")
b= input("Enter 2nd number")
c=input("Enter 3rd number")

num1= int(a)
num2= int(b)
num3= int(c)

if(num1>num2 or num1>num3):
    print("Number 1 is great")

elif(num2>num1 and num2>num3):
    print("Number 2 is great")

elif(num3>num1 and num3>num2):
    print("Number 3 is great") 

else:
    print("other than number 1 is great")
