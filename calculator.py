#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#create dictionary with +-/* as keys and names of functions as values
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbols in operations:
    print(symbols)

operation_symbol = input("Pick an operation from the line above: ")

def operate (num1, num2, operation_symbol):
    if operation_symbol == "+":
        final_value = add(num1,num2)
    elif operation_symbol == "-":
        final_value = subtract(num1,num2)
    elif operation_symbol == "*":
        final_value= multiply(num1,num2)
    elif operation_symbol == "/":
        final_value = divide(num1,num2)
    return final_value 


answer = operate(num1,num2,operation_symbol)
print(f"{num1} {operation_symbol} {num2} = {answer}")