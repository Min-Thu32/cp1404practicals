DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9
total_price = 0

item_number = int(input("Number of items: "))
while item_number < 1:
    print("Invalid number")
    item_number = int(input("Number of items: "))

for i in range(item_number):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > DISCOUNT_THRESHOLD:
    total_price *= DISCOUNT_RATE
print(f"Total price for {item_number} is ${total_price:.2f}")
