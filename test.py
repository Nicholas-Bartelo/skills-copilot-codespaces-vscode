import matplotlib.pyplot as plt
import numpy as np


print("hello world")

print("You are in the test.py file")

# Sample data
x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 7]

# Create scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')

# Show the plot
plt.show()