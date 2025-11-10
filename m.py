def is_even(number):
    return number % 2 == 0  # Returns True if even, False if odd

# Input from user
num = float(input("Enter  number: "))
if is_even(num):
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")