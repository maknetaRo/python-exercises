"""
7. Write a Python function that accepts a string and calculate the number
of upper case letters and lower case letters.
"""
def count_lower_upper(strng):
    lower = 0
    upper = 0
    strng = list(strng)
    for elem in strng:
        if elem.islower():
            lower += 1
        elif elem.isupper():
            upper += 1
    return "Lower letters: {}\n Upper letters: {}.".format(lower, upper)

strng = "Ala ma kota, a kot ma psa Burka."
print(count_lower_upper(strng))
