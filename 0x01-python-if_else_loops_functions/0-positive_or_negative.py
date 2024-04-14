import random

number = random.randint(-10,10)
print(number)
if number < 0:
    print(f"The number is {number}, It is a Negative number")
elif number > 0:
    print(f"The number is {number}, It is a Positive number")
else:
    print("The number is Zero /n")