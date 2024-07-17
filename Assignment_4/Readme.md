Assignment-4: Sampler for the Gaussian Distribution using the Inverse
CDF method

This Python script generates Gaussian distributed samples within a
specified interval \[a, b\] using the inverse cumulative distribution
function (CDF) method.

\## Prerequisites

\- Python 3.x - NumPy - Matplotlib - SciPy

\## Installation

1\. Install Python: Download and install Python from the official
website:
\[https://www.python.org/downloads/\](https://www.python.org/downloads/)

2\. Install Required Libraries: Open your command line interface and run
the following commands to install the required Python libraries: pip
install numpy pip install matplotlib pip install scipy

\## Usage

1\. Save the Code: Copy the provided Python code and save it in a file
named \'gaussian_sampling.py\'.

2\. Run the Code: Open your command line interface, navigate to the
directory where the \'gaussian_sampling.py\' file is saved, and run the
following command: python gaussian_sampling.py

3\. View the Output: After running the code, a histogram plot of the
Gaussian distributed samples will be displayed. The plot shows the
distribution of values generated within the specified interval \[a, b\].
The mean (mu) and standard deviation (sigma) of the Gaussian
distribution are calculated based on this interval.

\## Explanation

In this code firstly we generate random numbers in a uniform
distribution that is between 0 and 1. Then we define the interval
\[a,b\] in which we want to transform the numbers to gaussian samples.
We do this by the Inverse CDF method of the Gaussian distribution to
obtain samples from the Gaussian distribution. Finally, it plots a
histogram of the generated samples.

\## Customization

You can customize the following parameters in the code: - Interval \[a,
b\]: Modify the values of a and b to specify the desired interval for
the Gaussian distribution. - Number of Samples: Adjust the value of
num_samples to generate a different number of samples.
