'''Write a Python program to count the occurrences of each word in a given sentence 
string = “To change the overall look of your document. To change the look available in the gallery” '''

from collections import Counter
import re

# Given sentence
string = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase to make the count case-insensitive
string = string.lower()

# Remove punctuation (e.g., periods)
string = re.sub(r'[^\w\s]', '', string)

# Split the string into words
words = string.split()

# Count the occurrences of each word
word_count = Counter(words)

# Display the result
for word, count in word_count.items():
    print(f"'{word}': {count}")

'''
Output:- 'to': 2
         'change': 2
         'the': 3
         'overall': 1
         'look': 2
         'of': 1
         'your': 1
         'document': 1
         'available': 1
         'in': 1
         'gallery': 1 '''
