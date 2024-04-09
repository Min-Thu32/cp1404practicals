def main():
    user_dictionary = {}
    email = input("Email: ")

    while email != "":
        name = extract_name(email)
        is_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if is_correct == "" or is_correct == "y":
            user_dictionary[email] = name
        else:
            name = input("Name: ")
            user_dictionary[email] = name

        email = input("Email: ")

    print()
    for email, name in user_dictionary.items():
        print(f"{name} ({email})")


def extract_name(email):
    parts = email.split('@')
    name = parts[0].replace('.', ' ').title()
    return name


main()