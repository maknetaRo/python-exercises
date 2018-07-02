"""
12. Write a Python function that checks whether a passed string is palindrome
 or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward
 as forward, e.g., madam or nurses run.
 """

def is_palindrome(strng):
     new_strng = strng.replace(' ', '')
     return new_strng == new_strng[::-1]

if __name__=="__main__":
    strng = input("Enter a string to check if it's a palindorme: ")
    print(is_palindrome(strng))
