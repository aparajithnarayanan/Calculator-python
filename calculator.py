def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def divide(a,b):
    return a / b

def multiply(a,b):
    return a * b

print("select your operation")
print("1.add")
print("2.subtract")
print("3.divide")
print("4.multiply")

choice = input("Select opeation(1/2/3/4):")

num1 = int(input("Enter  you first number:"))
num2 = int(input("Enter your second number:"))

if choice == 1:
    print(num1, "+", num2, "=", add(num1,num2))
elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1,num2))
elif choice == 3:
    print(num1, "/", num2, "=", divide(num1,num2))
elif choice == 4:
    print(num1, "*", num2, "=", multiply(num1,num2))
else:
    print("Invalid operation")
        
    
            
