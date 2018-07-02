"""
10. Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

if __name__=="__main__":
    lst = [1,2,3,4,5,6,7,8,9]
    print(even_numbers(lst))
