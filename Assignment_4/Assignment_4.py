import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import special
from scipy.special import erfinv

# Define the Gaussian distribution parameters
#mu = 3  # Mean
#sigma = 2  # Standard deviation

# Define the interval [a, b]
a = float(input("Enter the lower bound of the interval (a): "))
b = float(input("Enter the upper bound of the interval (b): "))


mu = float(input("Enter (mu): "))
sigma = float(input("Enter (sigma): "))


# Calculate the mean and standard deviation based on the interval [a, b]
#mu = (a + b) / 2
#sigma = (b - a) / 6  # 99.7% of the data falls within 3 standard deviations

# Define the number of samples
num_samples = 10000000

# Generate uniform random numbers
uniform_samples = np.random.uniform(0, 1, num_samples)

# Define the inverse CDF function for the Gaussian distribution
#calculating inv cdf using inverse error function
def gaussian_inverse_cdf(x, mu, sigma):
    return mu + sigma * np.sqrt(2) * erfinv(2 * x - 1)

# Apply inverse CDF to the uniform random numbers to get Gaussian distributed samples within [a, b]
gaussian_samples = gaussian_inverse_cdf(uniform_samples, mu, sigma)
gaussian_samples = gaussian_samples[(gaussian_samples >= a) & (gaussian_samples <= b)]

# Plot histogram
plt.hist(gaussian_samples, bins=50, density=True, alpha=0.8, color='g')
plt.title('Histogram of Gaussian Samples')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()





gaussian_samples_sorted = np.sort(gaussian_samples)
cdf_values = np.arange(1, len(gaussian_samples_sorted) + 1) / len(gaussian_samples_sorted)

# Plot the CDF as a step function
plt.figure(figsize=(8, 6))
plt.step(gaussian_samples_sorted, cdf_values, where='post')
plt.title('CDF of Gaussian Samples')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.grid(True)
plt.show()