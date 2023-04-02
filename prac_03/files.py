user_name = input("Enter your name: ")
with open('name.txt', 'w') as out_file:
    out_file.write(user_name)

with open('name.txt', 'r') as out_file:
    user_name = out_file.read().strip()
print(f"Your name is {user_name}")

with open('numbers.txt', 'r') as out_file:
    first_number = int(out_file.readline())
    second_number = int(out_file.readline())
total = first_number + second_number
print(total)

with open('numbers.txt', 'r') as out_file:
    total = 0
    for line in out_file:
        total += int(line)
print(total)
