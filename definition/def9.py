"""
9. Write a Python function that takes a number as a parameter and check
the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than
 1 and that has no positive divisors other than 1 and itself.
"""
def is_prime(num):
    if num >= 2:
        for i in range(2, num+1):
            if num % i == 0 and i != num and i != 1:
                return False
        else:
            return True
    else:
        return False

print(is_prime(13))
print(is_prime(25))
