"""
1. Write a Python function to find the Max of three numbers.
"""
def max_of_three(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3

print(max_of_three(4, 6, 7))
print(max_of_three(11, 23, 7))
print(max_of_three(45, 16, 7))
