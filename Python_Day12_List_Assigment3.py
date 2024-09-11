#Write a Python program to find duplicate values from a list and display those

# Define the list with some duplicate values
my_list = [30, 80, 10, 70, 90, 10, 50, 30]

# Create an empty list to store duplicates
duplicates = []

# Iterate over the list
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j] and my_list[i] not in duplicates:
            duplicates.append(my_list[i])

# Print the duplicate values
if duplicates:
    print(f"Duplicate values in the list are: {duplicates}")
else:
    print("No duplicates found.")

#Output:- Duplicate values in the list are: [30, 10]
