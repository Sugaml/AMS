"""20. Write a program using recursive function to find nth Fibonacci number."""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

nth = 10
print("Fibonacci number at position", nth, "is:", fibonacci(nth))
