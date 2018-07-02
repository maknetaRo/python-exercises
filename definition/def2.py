"""2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""

def sum_all(lst):
    total = 0
    for elem in lst:
        total += elem
    return total

lst = [8, 2, 3, 0, 7]
print(sum_all(lst))
