# Underscores in Numbers when writing long numbers
num1 = 1_000_000_000
num2 = 2_500_000

# It's a constant variable whose values stays the same throughout the life of a program
NUM = 9_000_000_000

# Multiple assignment with one variable
coffee, ice_tea, energy_drink = 20, 5, 45


# Print out each variables with it values
print(num1)
print(num2)
print(NUM)
print(coffee)
print(ice_tea)
print(energy_drink)
print(coffee, energy_drink, ice_tea)

"""
Explanation
1️⃣ Underscores in numbers:

The numbers 1_000_000_000 and 2_500_000 include underscores for better readability.

In Python, underscores in numbers have no effect on calculations.

2️⃣ Constants (NUM):

While Python doesn’t enforce constants, writing them in uppercase (e.g., NUM) signals that the value should not be changed.

3️⃣ Multiple assignment:

The line coffee, ice_tea, energy_drink = 20, 5, 45 assigns values to three variables in one statement, making code more concise.

4️⃣ Printing values:

The print() statements output each variable’s value as an integer. The underscores are ignored when printing.

✅ Key Concepts:

Readability: Underscores make large numbers easier to read.

Best Practices: Using uppercase for constants.

Efficient Assignment: Multiple assignment in one line.
"""
