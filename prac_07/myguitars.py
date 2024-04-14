from guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")

    print("Unsorted Guitars:")
    display_guitars(guitars)

    guitars.sort()

    print("\nSorted Guitars (by year, oldest to newest):")
    display_guitars(guitars)


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

    main()
