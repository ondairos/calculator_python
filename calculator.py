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

def calculator(): #recursive function to start the program again
    num1 = int(input("What's the first number?: "))

    #display the symbols
    for symbols in operations:
        print(symbols)

    should_continue = True #flag

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calc_function = operations[operation_symbol] #use the function stored inside the dictionary with 1 line of code
        answer = calc_function(num1, num2) #store the answer

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to continue with a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
    
calculator()