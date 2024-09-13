# -------------------------------------------------------- #
# -- CALCULATOR FUNCTIONS -------------------------------- #
# -------------------------------------------------------- #

# Add function
def add(a, b):
    return a + b

# Subtract function
def sub(a, b):
    return a - b

# Multiply function with error handling to accept only integers
def mult(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    else:
        print("Error: Both arguments must be integers.")
        return None

# Divide function
def div(a, b):
    return a / b

# Square function
def square(a):
    return a * a


# -------------------------------------------------------- #

# -------------------------------------------------------- #
# -- MAIN FUNCTIONALITY ---------------------------------- #
# -------------------------------------------------------- #

a = None
b = None
op = None

while True:
    print("If your operation involves only one number [square, etc.], use a as your number and put b = 0.")
    a = input("Enter the first argument: ")
    op = input("Enter the operation: ")
    b = input("Enter the second argument: ")

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Invalid number argument... Only integers are allowed.")
        continue

    # decide function
    if op == "+":
        print("Sum: ", add(a, b))
    elif op == "-":
        print("Difference: ", sub(a, b))
    elif op == "*":
        result = mult(a, b)
        if result is not None:
            print("Product: ", result)
    elif op == "/":
        print("Quotient: ", div(a, b))
    elif op == "square":
        print("Square: ", square(a))
    else:
        print("Invalid operation...")

    q = input("Quit? [y/n] ")
    if q == "y" or q == "Y":
        break

# -------------------------------------------------------- #
