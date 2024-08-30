#Python program to check if a given number is an Armstrong number

def is_armstrong_number(num):
    # Convert number to string to easily iterate over digits
    num_str = str(num)
    # Number of digits
    num_digits = len(num_str)
    # Initialize sum of powers
    sum_of_powers = 0
    
    # Loop through each digit in the number
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the sum of the powers equals the original number
    return sum_of_powers == num

# Example usage
number_to_check = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")

'''
Output:- Enter a number to check if it's an Armstrong number: 521
         521 is not an Armstrong number.
         
         Enter a number to check if it's an Armstrong number: 370
         370 is an Armstrong number. '''
