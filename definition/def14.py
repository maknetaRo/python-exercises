"""
14. Write a Python function to check whether a string is a pangram or not.

Note : Pangrams are words or sentences containing every letter of the
alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""
def is_pangram(strng):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    strng = list(strng.lower())
    new_strng = []
    for letter in strng:
        if letter in alphabet:
            new_strng.append(letter)
    return len(set(new_strng)) == len(alphabet)

if __name__ == "__main__":
    strng = input("Enter a string to check if it's a pangram: ")
    print(is_pangram(strng))
