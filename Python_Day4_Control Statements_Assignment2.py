#Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

# Taking age input from the user
age = int(input("Enter your age: "))

# Checking if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

'''
Output:- Enter your age: 21
         You are eligible to vote.

         Enter your age: 17
         You are not eligible to vote yet. '''
