# Bayesian Inference with Beta Distribution

This repository contains Python code for performing Bayesian inference
using the Beta distribution. Bayesian inference is a statistical method
for updating beliefs about the parameters of a model based on evidence
(data). The Beta distribution is often used as a conjugate prior for the
binomial likelihood, making it ideal for modeling proportions or
probabilities.

## Libraries Used

The code utilizes the following libraries:

Numpy : For numerical computations and array operations. -
\*\*Matplotlib\*\*: For creating plots and visualizing the prior and
posterior distributions.

## Instructions

### Installation

Make sure you have Python installed on your system. You can download it
from \[python.org\](https://www.python.org/downloads/).

Install the required libraries using pip:

    pip install numpy matplotlib

## Running the Code

1\. Clone or download this repository to your local machine. 2. Open the Python script (\`bayesian_inference.py\`) in your preferred editor or IDE.

## Understanding the Code

\- \`calculate_mle(a, b)\`: Function to calculate the Maximum Likelihood
Estimate (MLE) given parameters a and b. - \`calculate_map(a, b,
num_heads, num_tails)\`: Function to calculate the Maximum A Posteriori
(MAP) estimate given parameters a, b, number of heads, and number of
tails. - \`beta(a, b, iter, n_heads, n_tails)\`: Function to generate
the Beta distribution given parameters a, b, number of iterations,
number of heads, and number of tails. - \`data\`: Example dataset
consisting of binary outcomes (0s and 1s). - \`n_heads\` and
\`n_tails\`: Number of heads and tails in the dataset, respectively. -
\`priors\`: List of different prior distributions specified as pairs of
parameters (a, b). - \`iter\`: Number of iterations for generating the
Beta distribution.

## Running the Code

\- Modify the \`data\` variable to use your own dataset if desired. -
Adjust the \`priors\` list to specify different prior distributions for
comparison. - Run the script. It will generate plots showing the prior
and posterior distributions for each specified prior, along with the
Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP)
estimates.

## Interpreting Results

\- The red curve represents the prior distribution. - The blue curve
represents the posterior distribution. - Dashed lines indicate the MLE
(red) and MAP (blue) estimates. - Compare the effect of different priors
on the resulting posterior distribution.
