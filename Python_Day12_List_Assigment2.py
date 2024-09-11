#Write a Python program to get the largest and smallest number from a list without builtin functions. 

# Define the list of numbers
my_list = [60, 70, 50, 90, 30]

# Initialize the variables for largest and smallest values
largest = my_list[0]
smallest = my_list[0]

# Loop through the list to find the largest and smallest values
for num in my_list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Print the results
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")

'''
Output:- The largest number is: 90
         The smallest number is: 30 '''
