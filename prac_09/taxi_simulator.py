from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    # Create a list of available taxis
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill = 0
    print("Let's drive!")

    while True:
        display_menu()
        choice = input(">>> ").lower()

        if choice == 'q':
            handle_quit(bill)
            break
        elif choice == 'c':
            current_taxi = handle_choose_taxi(taxis, bill)
        elif choice == 'd':
            bill = handle_drive(current_taxi, bill)
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill:.2f}")


def display_menu():
    print("q)uit, c)hoose taxi, d)rive")


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def handle_quit(bill):
    print(f"Total trip cost: ${bill:.2f}")


def handle_choose_taxi(taxis, bill):
    display_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))
    if 0 <= taxi_choice < len(taxis):
        print(f"Bill to date: ${bill:.2f}")
        return taxis[taxi_choice]
    else:
        print("Invalid taxi choice")
        print(f"Bill to date: ${bill:.2f}")
        return None


def handle_drive(current_taxi, bill):
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        print(f"Bill to date: ${bill:.2f}")
    else:
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
        bill += cost
        print(f"Bill to date: ${bill:.2f}")
    return bill


main()