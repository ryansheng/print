
#--------Part 1-----------# 

#print("The answer is: " + 42)
# cannot concatentate int: str(42)
"""favorite = input("Favorite number: ")
result = favorite + (10)
print(result)
"""
#TypeError; str(10)

#print("Hello World)

#Syntax Error: "hello World"

# age = int("twenty-five")
# Value Error; int("25")

#print(username)
# Name Error ; username = Ryan

#----------Part 2 -----------------------#

Error = "Thats not a valid number. Using 0 instead."
try:
    num1 = int(input("Enter Number 1: "))
except ValueError:
    print(Error)
    num1 = 0 
try:
    num2 = int(input("Enter number 2: "))
except ValueError:
    print(Error)
    num2 = 0
try:
    num3 = int(input("Enter number 3: "))
except ValueError:
    print(Error)
    num3 = 0
sum = num1 + num2 + num3
avg = sum / 3 
print(f"Your numbers: {str(num1) + ' , ' + str(num2) +' , ' + str(num3) }\n") 

print("Sum:" , f"{sum}")
print("Average:", f"{avg:.2f}")


