class cli_cal():
    def p(self):
        a = int(input("Give me the first number: "))
        b = int(input("Give me the second number: "))
        result = a + b 
        print(f"  {a} + {b} = {result}")  

    def m(self):
        a = int(input("Give me the first number: "))
        b = int(input("Give me the second number: "))
        result = a - b 
        print(f"  {a} - {b} = {result}")  

    def mul(self):
        a = int(input("Give me the first number: "))
        b = int(input("Give me the second number: "))
        result = a * b 
        print(f"  {a} * {b} = {result}")  

    def d(self):
        a = int(input("Give me the first number: "))
        b = int(input("Give me the second number: "))
        result = a / b 
        print(f"  {a} / {b} = {result}")  

    def xc(self):
        a = int(input("Give me the first number: "))
        b = int(input("Give me the second number: "))
        result = a % b 
        print(f"  {a} % {b} = {result}")  

# User Input

print("###  CLI Simple Calculator  ###")
print("a. For '+'")
print("b. For '-'")
print("c. For '*'")
print("d. For '/'")
print("e. For '%'")
print("f. For 'exit'.")

calculate = cli_cal()

while True:
    user_input = input("Enter your choice: ")

    if user_input == 'a':
        calculate.p()
    elif user_input == 'b':
        calculate.m()
    elif user_input == 'c':
        calculate.mul()
    elif user_input == 'd':
        calculate.d()
    elif user_input == 'e':
        calculate.xc()
    elif user_input == 'f':
        print("Exiting...")  
        break
    else:
        print("Invalid choice. Please select a valid option.")  
