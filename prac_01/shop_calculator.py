item_number = int(input("Number of items: "))
while item_number < 1:
    print("Invalid number")
    item_number = int(input("Number of items: "))

total_price = 0
for i in range(item_number):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9

print(f"Total prince for {item_number} items is ${total_price:.2f}")
