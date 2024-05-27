# Bayesian Modeling with PyMC - Probabilistic Python

### Probabilistic programming

Probabilistic programming is a paradigm that combines the techniques of probability theory with programming to create models that can reason and make decisions under uncertainty. This approach allows developers to build complex statistical models that can represent uncertain situations and make inferences from data. This repository aims to introduce probabilistic programming using Bayesian Modeling with PyMC.

Bayes' theorem provides the mathematical framework for updating beliefs.

<br>
<br>

$$
P(\theta \mid D) = \frac{P(D \mid \theta) P(\theta)}{P(D)}
$$

<br>
<br>

For common defitions using this approach visit the [DEFINITIONS.md](DEFINITIONS.md) file.


## Running the coin_flip.py Script

To run the script, make sure you have `pymc`, `arviz`, and `matplotlib` installed.

```
pip install pymc arviz matplotlib
```

Then, run the script:

```
python coin_flip.py
```

This will display the posterior distribution of `θ` (the probability of heads) and print a summary, which includes statistics like the mean, standard deviation, and credible intervals of the posterior distribution.


### Explanation

1. Import Libraries:

- `pymc` for Bayesian modeling.
- `matplotlib.pyplot` for plotting.
- `arviz` for plotting and summarizing the results.


2. Simulated Data:

- We simulate 10 coin tosses, with 7 heads (1s) and 3 tails (0s).


3. Model Definition:

- We define a PyMC model using a context manager (with `pm.Model()` as model).
- Prior: We use a Beta distribution with parameters

<br>

$$
\alpha = 1 \quad \text{and} \quad \beta = 1
$$

<br>

which is a uniform prior for the probability of heads (θ).

- Likelihood: We model the observed data as a Bernoulli distribution with parameter θ.

4.  Bayesian Inference:

- We run the MCMC sampler (`pm.sample(1000)`) to generate samples from the posterior distribution.

5. Plot and Summary:

- We use `az.plot_trace(trace)` to visualize the posterior distribution.

- We print a summary of the posterior distribution using `az.plot_trace(trace)`.
