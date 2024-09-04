''' Write a Python program to remove duplicate characters of a given string.
 Input = “String and String Function” Output: String and Function'''

def remove_duplicates(s):
    # Split the string into words
    words = s.split()
    # Use a set to track seen words
    seen_words = set()
    # Filter words that are not in the seen set
    unique_words = [word for word in words if word not in seen_words and not seen_words.add(word)]
    # Join the unique words into a single string
    return ' '.join(unique_words)

# Input string
input_string = "String and String Function"
output_string = remove_duplicates(input_string)

print(output_string)

#Output:- String and Function






