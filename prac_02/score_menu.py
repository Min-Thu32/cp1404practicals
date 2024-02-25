def main():

    score = 0
    menu = """(G)et a valid score (must be 0-100 inclusive)
    (P)rint result
    (S)how stars
    (Q)uit"""
    print(menu)

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")

        print(menu)
        choice = input(">>> ").upper()

    print("Farewell")


def show_stars(score):

    stars = "*" * int(score)
    print(stars)


def print_result(score):

    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
    print(f"The result is: {score}")


def get_valid_score():

    score = float(input("Enter your score (0-100): "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
    return score

main()
