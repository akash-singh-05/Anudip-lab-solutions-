''' Write a Python program to Get Only unique items from two sets. 
Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 
Output: {70, 40, 10, 50, 20, 60, 30} '''

# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Combine both sets into a list
combined_list = list(set1) + list(set2)

# Create a new list to maintain unique items
unique_items = []
seen = set()

# Iterate through the combined list and keep unique items
for item in combined_list:
    if item not in seen:
        unique_items.append(item)
        seen.add(item)

# Convert the result to a set (optional)
unique_items_set = set(unique_items)

# Print the result
print("Unique items from both sets:", unique_items_set)

#Output:- Unique items from both sets: {70, 40, 10, 50, 20, 60, 30}
