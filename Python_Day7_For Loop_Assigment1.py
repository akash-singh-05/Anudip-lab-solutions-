#Python program to check if the given string is a palindrome 

def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    length = len(s)
    
    # Check characters from the start and end moving towards the center
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

# Example usage
string_to_check = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(string_to_check):
    print(f"{string_to_check} is a palindrome.")
else:
    print(f"{string_to_check} is not a palindrome.")

'''
Output:- Enter a string to check if it's a palindrome: 12
         12 is not a palindrome.
         
         Enter a string to check if it's a palindrome: 121
         121 is a palindrome. '''
