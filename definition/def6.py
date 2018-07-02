"""
6.Write a Python function to check whether a number is in a given range
"""

def in_range(num):
    if num in range(number + 1):
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    number = int(input("Enter the max number: "))
    print(in_range(num))
