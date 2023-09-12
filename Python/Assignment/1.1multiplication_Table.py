# Get the number from the user
number = int(input("Enter a number: "))

# Print the multiplication table for the given number
print(f"Multiplication table for {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
