#Write a Python program that determines the largest of three numbers entered by the user.

# Taking three numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the largest number using the max() function
largest = max(num1, num2, num3)

# Printing the largest number
print(f"The largest number is {largest}.")

'''
Output:- Enter the first number: 52
         Enter the second number: 12
         Enter the third number: 45
         The largest number is 52.0. '''
