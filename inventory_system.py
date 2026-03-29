inventory = {
    "Milk": 10,
    "Bread": 8,
    "Eggs": 12,
    "Sugar": 15,
    "Tea": 20,
    "Rice": 25,
    "Biscuits": 18,
    "Oil": 10
}

MIN_THRESHOLD = 5

print("--- Stock Alert System ---")
sales_today = []

while True:
    item = input("Enter item sold (or 'done' to finish): ").strip().capitalize()
    if item.lower() == "done":
        break
    if item not in inventory:
        print(f"Item '{item}' not found in inventory. Try again.")
        continue
    try:
        quantity_sold = int(input(f"How many '{item}' were sold today? "))
        if quantity_sold < 0:
            print("Quantity cannot be negative.")
            continue
        sales_today.append((item, quantity_sold))
    except ValueError:
        print("Please enter a valid number.")

for item, quantity_sold in sales_today:
    inventory[item] -= quantity_sold

restock_candidates = []
for item, qty in inventory.items():
    if qty < MIN_THRESHOLD:
        restock_candidates.append(item)

seen = set()
unique_restock = []
for item in restock_candidates:
    if item not in seen:
        unique_restock.append(item)
        seen.add(item)

print("\n--- RESTOCK REPORT ---")
if unique_restock:
    print("Items to restock:")
    for item in unique_restock:
        print(f"  - {item} (Current stock: {inventory[item]})")
else:
    print("No items need restocking today.")

print("\nFull current inventory:")
for item, qty in inventory.items():
    status = "LOW" if qty < MIN_THRESHOLD else "OK"
    print(f"  {item}: {qty} ({status})")
