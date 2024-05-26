import pymc3 as pm
import numpy as np
import matplotlib.pyplot as plt

# Simulated data: 10 coin tosses with 7 heads and 3 tails
observed_data = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]

# Model definition
with pm.Model() as model:
    # Prior distribution for the probability of heads (theta)
    theta = pm.Beta('theta', alpha=1, beta=1)
    
    # Likelihood of observed data given theta
    y = pm.Bernoulli('y', p=theta, observed=observed_data)
    
    # Perform Bayesian inference
    trace = pm.sample(1000, return_inferencedata=False)

# Plot the posterior distribution
pm.traceplot(trace)
plt.show()

# Print a summary of the posterior distribution
print(pm.summary(trace))
