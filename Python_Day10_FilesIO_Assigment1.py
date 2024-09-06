#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_file_line_by_line(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())  # Strip removes any extra newline characters
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

# Example usage
read_file_line_by_line('ABC.txt')

'''
Output:- AKASH SINGH
          Address: Subhash Nagar, MIDC, Andheri East,
          Mumbai 400093
          E-mail: akashthakur05082003@gmail.com '''
