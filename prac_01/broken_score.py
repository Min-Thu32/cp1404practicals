"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score > EXCELLENT_SCORE:
    print("Excellent")
elif score > PASSABLE_SCORE:
    print("Passable")
else:
    print("Bad")
