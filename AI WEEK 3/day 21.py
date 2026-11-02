# Write a function called greet that takes a name
# and returns a greeting string
def greet(name):
    return f"Hello, {name}. Welcome to the program."

print(greet("Eric"))
print(greet("Amina"))
# Write a function called power(base, exp=2)
# that returns base raised to exp
def power(base, exp=2):
    return base ** exp

# Use a list comprehension to get all even numbers from 1 to 30
evens = [n for n in range(1, 31) if n % 2 == 0]
print(evens)

# Now get the squares of those even numbers
squares = [n**2 for n in evens]
print(squares)
# Write a function that takes a list of scores
# and returns the average, highest, and lowest
def analyse(scores):
    return {
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores)
    }

result = analyse([78, 91, 63, 85, 72])
for k, v in result.items():
    print(f"{k}: {v}")
    def greet(name):
     return f "Hello, {name}!"

print(greet("Amerix"))
print(greet("SMP Member"))
print(greet("Guest"))