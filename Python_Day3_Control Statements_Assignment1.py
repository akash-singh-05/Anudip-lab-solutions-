#Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

# Taking input from the user
number = int(input("Enter a number: "))

# Checking if the number is even or odd
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

'''
Output:- Enter a number: 69
         Odd

         Enter a number: 44
         Even  '''

