#Write a python program to check whether a number is palindrome or not? 

def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Example usage
number = int(input("Enter a number to check if it is a palindrome: "))

if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

'''
Output:- Enter a number to check if it is a palindrome: 54
         54 is not a palindrome.

         Enter a number to check if it is a palindrome: 88
         88 is a palindrome. '''
