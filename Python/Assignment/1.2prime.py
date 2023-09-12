# Get the number from the user
number = int(input("Enter a number: "))

# Check if the number is less than 2 (prime numbers are greater than 1)
if number < 2:
    print(f"{number} is not a prime number.")
else:
    # Check for factors from 2 to the square root of the number
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    # Display the result
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
