from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    while True:
        new_guitar = input_guitar()
        if new_guitar is None:
            break
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:<30} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def input_guitar():
    name = input("Name: ")
    if name == "":
        return None
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return Guitar(name, year, cost)


main()
