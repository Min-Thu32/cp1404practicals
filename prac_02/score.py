def main():

    score = float(input("Enter score: "))
    score_calculate(score)

    import random
    result = random.randint(0, 100)
    print(f"Result: {result}")


def score_calculate(score):

    if score < 0 or score >= 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
