import array as arr

values =arr.arrray('i',[1,2,3,4,5])
print(f"The length of array is {len(values)}")


values= arr.array('i',[])
n= int(input("Enter length of array:"))

for i in range(n):
    x= int(input(f"Enter {i+1} value:"))
    values.append(x)
    print(values)
    

