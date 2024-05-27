def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example: Generate the first 10 Fibonacci numbers
print(list(fibonacci(10)))