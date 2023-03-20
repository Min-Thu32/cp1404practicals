MENU = """(H)ello
(G)oodbye
(Q)uit"""

username = input("Enter Name: ")

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {username}")
    elif choice == "G":
        print(f"Goodbye {username}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
