import numpy as np
import matplotlib.pyplot as plt


# Parameters of the normal distribution
mean = 0  # Mean value
std_dev = 1  # Standard deviation
num_samples = 1000  # Number of samples

# Generate random numbers distributed according to the normal distribution
data = np.random.normal(mean, std_dev, num_samples)

# Create a histogram
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
