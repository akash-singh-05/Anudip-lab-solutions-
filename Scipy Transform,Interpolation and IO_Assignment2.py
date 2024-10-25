'''Write a python program using Interpolation to fill in missing values in the data frame.
After that store the data frame into a MATLAB file using SciPy IO.Then display the contents from the MATLAB file. 
Input: df = pd.DataFrame({"Math":[12, 4, 7, None, 2], "English":[4, 3, 57, 3, None], "Hindi":[20, 16, None, 3, 8], "Science":[14, 3, None, None, 6]})'''

import pandas as pd
import numpy as np
from scipy.io import savemat, loadmat

# Create the DataFrame
df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

# Interpolate to fill in missing values
df_interpolated = df.interpolate()

# Display the DataFrame after interpolation
print("\nDataFrame after interpolation:")
print(df_interpolated)

# Save the DataFrame to a MATLAB file
# Convert the DataFrame to a dictionary
data_to_save = {col: df_interpolated[col].to_numpy() for col in df_interpolated.columns}
savemat('interpolated_data.mat', data_to_save)

# Load the contents from the MATLAB file
loaded_data = loadmat('interpolated_data.mat')

# Display the contents from the MATLAB file
print("\nContents of the MATLAB file:")
for key in loaded_data:
    if not key.startswith('__'):  # Skip meta keys
        print(f"{key}: {loaded_data[key]}")

'''Output:-
DataFrame after interpolation:
   Math  English  Hindi  Science
0  12.0      4.0   20.0     14.0
1   4.0      3.0   16.0      3.0
2   7.0     57.0    9.5      4.0
3   4.5      3.0    3.0      5.0
4   2.0      3.0    8.0      6.0

Contents of the MATLAB file:
Math: [[12.   4.   7.   4.5  2. ]]
English: [[ 4.  3. 57.  3.  3.]]
Hindi: [[20.  16.   9.5  3.   8. ]]
Science: [[14.  3.  4.  5.  6.]]'''
