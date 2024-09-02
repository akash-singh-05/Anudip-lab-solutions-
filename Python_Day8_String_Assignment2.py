'''Write a Python program to remove a newline in Python
 String = "\nBest \nDeeptech \nPython \nTraining\n"'''

# Given string with newline characters
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove all newline characters
cleaned_string = string.replace("\n", " ")

# Optionally, strip any leading or trailing spaces (due to leading/trailing newlines)
cleaned_string = cleaned_string.strip()

# Display the result
print(cleaned_string)

#Output:- Best  Deeptech  Python  Training
