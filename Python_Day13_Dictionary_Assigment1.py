'''Write a Python program and calculate the mean of the below dictionary.
 test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 
Output: 6.2'''

# Define the dictionary
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

# Calculate the sum of the values
total = sum(test_dict.values())

# Calculate the mean
mean = total / len(test_dict)

# Print the result
print(f"Mean: {mean}")

#Output:- Mean: 6.2
