import numpy as np
import matplotlib.pyplot as plt


# Generate two sets of random data
num_points = 100
x_data = np.random.rand(num_points)
y_data = np.random.rand(num_points)

# Create a scatter plot
plt.scatter(x_data, y_data, c='blue', alpha=0.5)
plt.title('Scatter Plot of Random Data')
plt.xlabel('X Data')
plt.ylabel('Y Data')
plt.show()
