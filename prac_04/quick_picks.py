import random

NUMBERS_PER_QUICK_PICK = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

quick_picks = int(input("How many qick picks? "))
for i in range(quick_picks):
    quick_pick_numbers = []
    while len(quick_pick_numbers) < NUMBERS_PER_QUICK_PICK:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in quick_pick_numbers:
            quick_pick_numbers.append(number)
    quick_pick_numbers.sort()

    for number in quick_pick_numbers:
        print(f"{number:2}", end=' ')
    print()
