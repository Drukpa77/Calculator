usr_choice = 0
choice_str = """
Choose an option from the list below:
1 - Add
2 - Subtract
3 - Divide
4 - Multiply

Your option:"""


def add(nums):
    return x + y


def subtract():
    return x - y


def divide():
    return x / y


def multiply():
    return x * y


def get_input():
    try:
        usr_val = int(input("Please enter the mathematical expression: "))
        return usr_val
    except ValueError:
        print("Please enter a number as the input")


def main():
    while True:
        try:
            usr_choice = int(input(choice_str))

            if(usr_choice > 4 or usr_choice < 1):
                print("Please enter a valid option")
            break
        except ValueError:
            print("Please enter a number as the input")

    if(usr_choice == 1):
        usr_nums = get_input()
        print(usr_nums)


if (__name__ == "__main__"):
    main()
