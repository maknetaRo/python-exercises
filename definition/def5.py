"""
5. Write a Python function to calculate the factorial of a number
(a non-negative integer). The function accepts the number as an argument.
"""
def factorial(num):
    total = 1
    for i in range(1, num+1):
        total *= i
    return total

print(factorial(5))
