'''Using input() function take one number from the user and
 using ternary operators check whether the number is even or odd '''

# Taking input from the user
number = int(input("Enter a number: "))

# Checking if the number is even or odd using a ternary operator
result = "Even" if number % 2 == 0 else "Odd"

# Printing the result
print(f"The number {number} is {result}.")


'''Output:- Enter a number: 69
        The number 69 is Odd.'''

