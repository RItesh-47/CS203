import numpy as np
import matplotlib.pyplot as plt

def calculate_mle(a, b):
    if a == 1 and b == 1:
        return 0.5  # Uniform distribution if a=b=1
    else:
        return (a - 1) / (a + b - 2)

def calculate_map(a, b, num_heads, num_tails):
    if a + b + num_heads + num_tails - 2 == 0:  # Handle denominator equals 0
        return None
    else:
        return (a + num_heads - 1) / (a + b + num_heads + num_tails - 2)

def beta(a, b, iter, n_heads, n_tails):
    values = []
    theta = np.linspace(0, 1, iter)
    for t in theta:
        y = (t ** (a - 1)) * ((1 - t) ** (b - 1)) / (np.math.gamma(a) * np.math.gamma(b) / np.math.gamma(a + b))
        values.append(y)
    return theta, values

data = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0]
n_heads = sum(data)
n_tails = len(data) - n_heads
priors = [
    [2, 5],
    [5, 2],
    [1, 1],
    [2, 2]
]

iter = 10000

for prior in priors:
    a = prior[0]
    b = prior[1]

    # likelihood
    theta, likelihood = beta(a, b, iter, n_heads, n_tails)
    likelihood_normalised = [i / sum(likelihood) for i in likelihood]
    max_likelihood = n_tails/len(data)

    # posterior
    theta, posterior = beta(a + n_tails, b + n_heads - n_tails, iter, n_heads, n_tails)
    posterior_normalized = [i / sum(posterior) for i in posterior]
    max_posterior = calculate_map(a, b, n_heads, n_tails)

    plt.plot(theta, likelihood_normalised, 'r', label='Prior' if prior == priors[0] else None)
    plt.plot(theta, posterior_normalized, 'b', label='Posterior' if prior == priors[0] else None)

    plt.axvline(x=max_likelihood, color='r', linestyle='--', linewidth=1, label='MLE')
    plt.axvline(x=max_posterior, color='b', linestyle='--', linewidth=1, label='MAP')
    plt.title(f'Combined Prior and Posterior Distributions for a={a} and b={b}')
    plt.xlabel('Theta')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()
