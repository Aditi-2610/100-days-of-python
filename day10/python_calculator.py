
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations_dictionary = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def check_num_is_a_number(num):
    try:
        # Attempt to convert the input string to an integer
        num = float(num)
        return num
    except ValueError:
        # If a ValueError occurs during conversion, it means the input is not a valid integer
        print(f"The input '{num}' is not an integer. Try again!")
        num2 = input("Enter your number again: ")
        return check_num_is_a_number(num2)

def choose_operation():
    #making sure the entered string is a valid operation
    selected_operation = input("Pick an operation: ")
    if not selected_operation in operations_dictionary :
        print("Not a valid operation. Select again: ")
        return choose_operation()
    return selected_operation


# print(operations_dictionary["*"](4,6))
print(logo)
def calculator():
    # check the first number
    first_num = input("Whats the first number ?  ")
    first_num = check_num_is_a_number(first_num)


    # set the continue var
    to_continue = 'y'

    # let while loop run until user gives valid decision inputs
    while to_continue == 'y':
        print(" + \n - \n * \n / \n")

        # checking if the entered operation is valid
        operation = choose_operation()


        # checking if the secind number is valid
        second_num = input("Whats the second number ?  ")
        second_num = check_num_is_a_number(second_num)

        # performing the calculation
        result = operations_dictionary[operation](first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {result}" )

        # asking user if they want to continue
        to_continue = input(f"Type 'y' to continue calculating with {result}"
                            f"or type 'n' to start a new calculation or any other letter to exit:  ").lower()
        if to_continue == 'y':
            first_num = result
        elif to_continue == 'n':
            print("\n" * 30)
            print(logo)  #just adds 20 lines to make it look like a new page
            calculator()
        else:
            exit()





calculator()