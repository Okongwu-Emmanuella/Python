import random

number = random.randint(-10000, 10000)
Last_digit = str(number)
num = Last_digit[-1]


if num > "5":
    print(f"Last digit of {number} is {Last_digit[-1]} and is greater than 5")
elif num == "0":
    print(f"Last digit of {number} is {Last_digit[-1]} and is 0")
else:
    print(f"Last digit of {number} is {Last_digit[-1]} and is less than 6 and not 0")