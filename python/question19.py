
"""19. Write a program using recursive function to find factorial of a number."""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
print("Factorial of", number, "is", factorial(number))

