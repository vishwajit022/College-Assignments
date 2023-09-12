import math

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD using math.gcd()
gcd = math.gcd(num1, num2)

# Display the GCD
print(f"The GCD of {num1} and {num2} is {gcd}")