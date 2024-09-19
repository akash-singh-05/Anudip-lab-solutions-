'''Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions.
Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 
Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12])'''

import numpy as np

# Define the temperature array
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, -4, -12])

# Define the temperature thresholds
hot_threshold = 35
cold_threshold = 5

# Identify the days with extreme temperatures
hot_days = temperatures > hot_threshold
cold_days = temperatures < cold_threshold

# Combine the hot and cold days
extreme_days = hot_days | cold_days

# Print the results
print("Temperatures:", temperatures)
print("Extreme temperature days (hot or cold):", temperatures[extreme_days])

'''
Output:- Temperatures: [ 32.5  34.2  36.8  29.3  31.   38.7  23.1  18.5  22.8  37.2  -4.  -12. ]
         Extreme temperature days (hot or cold): [ 36.8  38.7  37.2  -4.  -12. ]'''
