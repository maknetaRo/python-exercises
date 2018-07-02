"""3. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""

def multiply_all(lst):
    total = 1
    for num in lst:
        total *= num
    return total


lst = [8, 2, 3, -1, 7]
print(multiply_all(lst))
