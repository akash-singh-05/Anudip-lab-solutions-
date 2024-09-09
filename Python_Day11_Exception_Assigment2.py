#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    user_input = input("Enter an integer: ")
    user_integer = int(user_input)  # Attempt to convert the input to an integer
    print(f"You entered the integer: {user_integer}")

except ValueError:
    print("Error: Invalid input! You must enter a valid integer.")

'''
Output:- Enter an integer: 55
         You entered the integer: 55
         Enter an integer: akash
         Error: Invalid input! You must enter a valid integer.'''
