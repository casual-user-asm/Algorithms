"""
    Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem.
    It is a fundamental concept in computer science and is widely used in solving problems that can be divided into smaller, identical sub-problems. 
"""

def fuctorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fuctorial(number-1)


def palindrom(word):
    if len(word) <= 1:
        return 'This is palindrom'
    elif word[0] == word[-1]:
        return palindrom(word[1:-1])
    else:
        return 'This is not palindrom'


def powers_of_number(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / powers_of_number(base, -exponent)
    else:
        return base * powers_of_number(base, exponent - 1)
