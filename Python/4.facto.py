def facto(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

number = int(input("Enter a number: "))
result = factorial_recursive(number)
print(f"The factorial of {number} is {result}")
