def main():

    minimum_password_length = 7

    while True:
        password = get_password()
        if len(password) < minimum_password_length:
            print("Password is too short. Please try again.")
        else:
            for i in range(len(password)):
                print_asterisks()
            break


def get_password():
    password = input("Enter your password: ")
    return password


def print_asterisks():
    print("*", end='')


main()
