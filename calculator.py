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



print(f"{num1} {operation_symbol} {num2} = {answer}")