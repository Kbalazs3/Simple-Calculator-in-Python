import time

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def is_valid_operation(operation):
        operations = ('+', '-', '*', '/')
        return operation in operations


def ask_for_a_number(force_valid_input):
    while True:
        inp = input("Please provide a number: ")
        if is_number(inp):
            return float(inp)
        else:
            if not force_valid_input:
                return None
            print("This didn't look like a number, try again.")

def ask_for_an_operation(force_valid_input):
    while True:
        operation = input("Please provide an operation (one of +, -, *, /)! ")
        if is_valid_operation(operation):
            return operation
        else:
            if not force_valid_input:
                return None
            print("Unknown operation.")


def calc(operation, a, b):
    if not is_valid_operation(operation) or not is_number(a) or not is_number(b):
        return None
    elif operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b != 0:
            result = a / b
        else:
            print('Error! Division by zero!')
    return result

def simple_calculator():
  #  main_menu()
    time.sleep(2)
    while True:
        a = ask_for_a_number(force_valid_input=False)
        if not a:
            break
        op = ask_for_an_operation(force_valid_input=True)
        b = ask_for_a_number(force_valid_input=True)
        result = calc(op, a, b)
        if result:
            print(f"The result is {calc(op, a, b)}")
            time.sleep(5)
           # main_menu()


# def main_menu():
  #  print()
   # print("    MAIN MENU\n   Start Calculating\n      Quit")
    #print()
    #main_question = ""
    #while main_question != 's' or 'q':
     #   main_question = input("Enter s to start, or q to quit:\n ")
      #  if main_question == "s":
       #     break
        # elif main_question == "q":
          #  print()
           # print("Bye-Bye")
            # time.sleep(3)
            # exit(0)



if __name__ == '__main__':
    simple_calculator()


