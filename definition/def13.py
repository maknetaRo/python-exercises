"""
13.Write a Python function that prints out the first n rows of Pascal's
 triangle.
Note : Pascal's triangle is an arithmetic and geometric figure first
 imagined by Blaise Pascal.
"""
# prints lists
def pascal_triangle(num):
    lst = [1]
    for i in range(1, num+1):
        print(lst)
        new_lst = []
        new_lst.append(lst[0])
        for i in range(len(lst)-1):
            new_lst.append(lst[i]+lst[i+1])
        new_lst.append(lst[-1])
        lst = new_lst
    return lst

num = int(input("How many lines of Pascal's Triangle would you like to print out:"))
print(pascal_triangle(num))
