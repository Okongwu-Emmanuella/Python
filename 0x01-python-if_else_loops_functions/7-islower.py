"""
Write a function that checks for lowercase character.

Prototype: def islower(c):
Returns True if c is lowercase
Returns False otherwise
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
You don’t need to understand _
"""
import random
alphabet = ["a", "B", "c", "D"]


def islower(c):
    for let in range(97, 122):

        letter = chr(let)

        if c in letter:
            return True
        else:
            return False


choice = random.choice(alphabet)
result = islower(choice)
print(f"{choice} is {result}")

