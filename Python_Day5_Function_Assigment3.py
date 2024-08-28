#Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random

# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]

# Display the numbers
print("The 5 random numbers are:", numbers)

# Find and display the maximum and minimum
print("The maximum number is:", max(numbers))
print("The minimum number is:", min(numbers))

'''
Output:- The 5 random numbers are: [4, 66, 11, 5, 68]
         The maximum number is: 68
         The minimum number is: 4 '''
