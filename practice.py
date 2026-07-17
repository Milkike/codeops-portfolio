# Practice 1: if / elif / else
age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")


# Practice 2: for loop
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)


# Practice 3: while loop
count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# Practice 4: Modulo (%)
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Practice 5: Function
def greet(name):
    return "Hello " + name


message = greet("Milki")
print(message)