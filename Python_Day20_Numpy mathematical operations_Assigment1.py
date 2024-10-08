'''Calculate the total revenue generated by two product categories in a store 
Input: category1_revenue = np.array([500, 600, 700, 550]) 
category2_revenue = np.array([450, 700, 800, 600])'''

import numpy as np

# Input revenues for both categories
category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])

# Calculate the total revenue by adding both arrays
total_revenue = category1_revenue + category2_revenue

# Output the result
print("Total Revenue:", total_revenue)

#Output:- Total Revenue: [ 950 1300 1500 1150]
