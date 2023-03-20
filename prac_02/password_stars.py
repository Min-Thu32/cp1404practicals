minimum_password_length = 7

while True:
    password = input("Enter your password: ")
    if len(password) < minimum_password_length:
        print("Password is too short. Please try again.")
    else:
        for i in range(len(password)):
            print("*", end='')
        break
