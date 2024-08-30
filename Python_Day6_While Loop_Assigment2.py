#Write a python program finding the factorial of a given number using a while loop

def factorial(n):
    # Initialize the result to 1 (factorial of 0 and 1 is 1)
    result = 1
    
    # Ensure n is a non-negative integer
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    # Compute factorial using a while loop
    while n > 1:
        result *= n
        n -= 1
    
    return result

# Example usage
number = int(input("Enter a number to find its factorial: "))

print(f"The factorial of {number} is {factorial(number)}")

'''
Output:- Enter a number to find its factorial: 5
         The factorial of 5 is 120 '''
