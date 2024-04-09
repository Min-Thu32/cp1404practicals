from guitar import Guitar


# Test function for get_age() and is_vintage()
def test_guitar_methods():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1000.00)

    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")

    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")


# Run the test
test_guitar_methods()
