# ============================
# Exercise 1 - Unique Cities
# ============================

cities = [
    "Addis Ababa",
    "Adama",
    "Hawassa",
    "Addis Ababa",
    "Bahir Dar",
    "Adama"
]

unique_cities = set(cities)

print("Unique Cities:")
for city in unique_cities:
    print(city)

print("Total Unique Cities:", len(unique_cities))


# ============================
# Exercise 2 - Price Report
# ============================

prices = {
    "Bread": 45,
    "Milk": 90,
    "Eggs": 180,
    "Sugar": 120,
    "Rice": 350
}

print("\nPrice Report")
for item, price in prices.items():
    print(f"{item}: {price} ETB")


# ============================
# Exercise 3 - Tax
# ============================

prices_list = [100, 250, 400, 80]

tax_prices = [price * 1.15 for price in prices_list]

print("\nPrices with Tax")
print(tax_prices)


# ============================
# Exercise 4 - Cheap Items
# ============================

cheap = [price for price in prices_list if price < 200]

print("\nCheap Prices")
print(cheap)


# ============================
# Exercise 5 - Write & Read
# ============================

with open("names.txt", "w") as file:
    file.write("Abebe\n")
    file.write("Almaz\n")
    file.write("Dawit\n")

print("\nNames")

with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())


# ============================
# Exercise 6 - Safe Division
# ============================

try:
    number = int(input("\nEnter a number: "))
    result = 1000 / number
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Number cannot be zero.")
else:
    print("Result =", result)
finally:
    print("Program Finished")