#add func
def add (x, y):
    return x + y

def subtrack (x , y):
    return x - y

def multiply (x , y):
    return x * y

def divide (x, y):
    return x / y

print ("Select a operation.")
print ("1. Add")
print ("2. Subtrackt")
print ("3. Multiply")
print("4. Divide")

while True:
    choice = input("Please enter choice (1/2/3/4)")

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("İnavalid input. Please enter a number.")
            continue

        if(choice == "1"):
            print(f"{num1} + {num2} = {add (num1, num2)}")
        elif (choice == "2"):
            print(f"{num1} - {num2} = {subtrack (num1, num2)}")
        elif(choice == "3"):
            print(f"{num1} * {num2} = {multiply (num1, num2)}")
        elif(choice == "4"):
            print(f"{num1} / {num2} = {divide (num1, num2)}")
    
        nextCalculation = input("Do you wanna make another calculation (yes/no)")
        if(nextCalculation == "no"):
            break
    else:
        print("Inavalid Input.")