"""
8. Write a Python function that takes a list and returns a new list
 with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""
def unique_list(lst):
    unique_list = []
    for elem in lst:
        if elem not in unique_list:
            unique_list.append(elem)
    return unique_list

lst= [1,2,3,3,3,3,4,5]
print(unique_list(lst))
