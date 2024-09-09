#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    result = numerator / denominator
    print(f"The result is: {result}")
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

'''
Output:- Enter the numerator: 55
         Enter the denominator: 44
         The result is: 1.25 
         Enter the numerator: 55
         Enter the denominator: 0
         Error: Division by zero is not allowed.'''
