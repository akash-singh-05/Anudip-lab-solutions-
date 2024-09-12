'''Write a Python script to concatenate the following dictionaries to create a new one. 
Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

# Given dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Creating a new dictionary by concatenating the dictionaries
concatenated_dict = {}

# Update the empty dictionary with each of the given dictionaries
concatenated_dict.update(dic1)
concatenated_dict.update(dic2)
concatenated_dict.update(dic3)

# Display the result
print(concatenated_dict)

#Output:- {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
