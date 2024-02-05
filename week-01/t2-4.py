# 4.1

favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print(f"I really love {pizza} pizza!")

print("\nI really love pizza!")

# 4.2

animals = ["spider monkey", "lemur", "giraffe"]

# Print each animal.
for animal in animals:
    print(animal)

print("\n")

# Print a statement about each animal.
for animal in animals:
    print(f"A {animal} has a long tail.")

print("\nAll of these animals have long tails.")

# 4.3

numbers = list(range(1, 21))

for number in numbers:
    print(number)

# 4.5
    
numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4.6

odd_numbers = list(range(1, 20, 2))

for number in odd_numbers:
    print(number)