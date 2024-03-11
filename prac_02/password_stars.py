"""Password masking module"""

MINIMUM_PASSWORD_LENGTH = 8


def main():

    """Prompt users to enter a password and converting it with asterisks"""

    while True:
        password = get_password()
        if len(password) < MINIMUM_PASSWORD_LENGTH:
            print("Password is too short. Please try again.")
        else:
            for i in range(len(password)):
                print_asterisks()
            break


def print_asterisks():
    """Function for printing asterisks"""
    print("*", end='')


def get_password():
    """Function for entering password"""
    password = input("Enter your password: ")
    return password


main()
