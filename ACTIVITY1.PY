name ="Penguin"
age =15
is_student=True
weight=38.5

print("Name :", name)
print("Data Type of Name is",type(name) )
print("Age:", age)
print("Data Type of Age is",type(age))
print("is_student:".is_student)
print("Data Type of is_student is",type(is_student))
print("Weight:",weight)
print("Data Type of Weight is",type(weight))

print("\n After type casting...")
age=str(age)
print(age)
print("Data Type of Age is",type(age))
weight=int(weight)
print(weight)
print("Data Type of Weight is",type(weight))
#OPERATORS
num1=45
num2=3

print("Number 1", num1)
print("Number 2", num2)
print("Addition:",num1+num2)
print("Difference:",num1-num2)
print("Product:",num1*num2)
print("Devision:",num1/num2)
print("FloorDevision:",num1//num2)
print("Modulus Operation:",num1%num2)
print("Square:",num2**num2)
print("Square Root:",num1**0.5)

print("Equal?",num1==num2)
print(num1<num2)
print(num1>num2)
print(num1=num2)
result=7+3/2(2-4)//4-5%44
print(result)

#String OPeration
first_name="Codingal"
last_name="Educations"
full_name=first_name+last_name #concatenation
example="Haa"*5 #multiplication

print("First Name:",first_name)
print("Last Name:",last_name)
print("Full Name:",full_name)
print("String Multiplied 5 times gives this result :",example)

word='Coding'
print("Lenght of String:",len(word))
print("First Letter of String:",word[0])
print("Last Letter of String:",word[5])
print("String Sliced:",word[0:3])

#Swapping operation
#Take input values from user
x=input("Enter Value of x:")
y=input("Enter Value of y:")

#Swapping
temp=x
x=y
y=temp
#Displaying results after swapping
print("value of x after swapping",x)
print("value of y after swapping",y)