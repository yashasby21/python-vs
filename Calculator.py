def add(x,y):
    return x + y


def sub(x,y):
    return x - y


def mul(x,y):
    return x * y


def div(x,y):
    return x / y


while True:
    print("Options: ")
    print("Enter 'add' for addition ")
    print("Enter 'sub' for subtraction ")
    print("Enter 'mul' for multiplication ")
    print("Enter 'div' for division ")
    print("Enter 'quit' to end ")
    user_input=input(': ')

    if user_input == 'quit':
        break

    if user_input in ("add","sub","mul","div"):
        num1= float(input("Enter first number: "))
        num2= float(input("Enter second number: "))
        
        if user_input == "add":
            print("Result: ",add(num1,num2))
        elif user_input == "sub":
            print("Result: ",sub(num1,num2))
        elif user_input == "mul":
            print("Result: ",mul(num1,num2))
        elif user_input == "div":
            print("Result: ",div(num1,num2))
        else:
            print("Invalid input")
        