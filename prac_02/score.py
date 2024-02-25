import random


def main():

    score = float(input("Enter score: "))
    score_calculate(score)

    random_score()


def random_score():
    result = random.randint(0, 100)
    print(f"Result: {result}")


def score_calculate(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")


main()
