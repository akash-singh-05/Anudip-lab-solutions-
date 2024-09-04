'''Write a Python program to Count all letters, digits, and special symbols from the given string
 Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3 '''

def count_characters(s):
    letters = digits = special_symbols = 0

    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1

    return letters, digits, special_symbols

# Input string
input_string = "P@#yn26at^&i5ve"
letters, digits, special_symbols = count_characters(input_string)

print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special Symbols: {special_symbols}")

'''
Output:- Letters: 8
         Digits: 3
         Special Symbols: 4'''

