stock = {}

# Read File
try:
    with open("stock.txt", "r") as file:
        for line in file:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)
except FileNotFoundError:
    print("No stock file found. Starting with empty inventory.")


# Function
def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount


# Sample Updates
adjust("Paracetamol", 5)
adjust("Vitamin C", -2)
adjust("Bandage", 4)


# Low Stock Report
print("\nCurrent Inventory")

for item, qty in stock.items():
    print(item, qty)

print("\nLow Stock Items")

low_stock = [item for item, qty in stock.items() if qty < 10]

for item in low_stock:
    print(item)


# Save File
with open("stock.txt", "w") as file:
    for item, qty in stock.items():
        file.write(f"{item},{qty}\n")

print("\nInventory Updated Successfully.")