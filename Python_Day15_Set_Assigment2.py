'''Write a Python program to Return a set of elements present in Set A or B, but not both.
Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 
Output: {20, 70, 10, 60}'''

# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Get the symmetric difference
symmetric_difference = set1.symmetric_difference(set2)

# Print the result
print("Elements present in set1 or set2, but not both:", symmetric_difference)

#Output:- Elements present in set1 or set2, but not both: {20, 70, 10, 60}
