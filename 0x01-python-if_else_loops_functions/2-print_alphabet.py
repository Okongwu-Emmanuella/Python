"""
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module
"""
# for chr(range(''))

for num in range(97, 123):

    print(chr(num), end="")


'''hex_string = '0F'
decimal_value = int(hex_string, 16)
print(f"Value in hexadecimal: {hex_string}")
print(f"Value in decimal: {decimal_value}")'''
