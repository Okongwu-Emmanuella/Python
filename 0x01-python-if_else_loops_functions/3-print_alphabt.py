"""
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

Print all the letters except q and e
You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module
"""
for num in range(97, 123):
    if num == 101 or num == 113:
        pass
    else:
        print(chr(num), end="")