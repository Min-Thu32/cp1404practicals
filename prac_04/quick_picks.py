import random

NUMBERS_PER_QUICK_PICK = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
    quick_pick_numbers = random.sample(range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1), NUMBERS_PER_QUICK_PICK)
    quick_pick_numbers.sort()

    for number in quick_pick_numbers:
        print(f"{number:2}", end=' ')
    print()
