# Definitions

## Bayesian Inference

Bayesian inference is a method of statistical inference in which Bayes' theorem is used to update the probability for a hypothesis as more evidence or information becomes available. It is a powerful technique for learning from data, making predictions, and making decisions under uncertainty. The core idea is to combine prior knowledge (prior probability) with new evidence (likelihood) to form a posterior probability, which represents the updated belief after observing the data.

Bayes' Theorem:

Bayes' theorem provides the mathematical framework for updating beliefs

$$
P(\theta \mid D) = \frac{P(D \mid \theta) P(\theta)}{P(D)}
$$

1. Prior Probability (Prior): Denoted as 
`P(θ)`, it represents the initial belief about the parameter `θ` before any data is observed. The prior can be based on previous studies, expert knowledge, or even non-informative (uniform) if no prior information is available.

2. Likelihood: Denoted as `P(D∣θ)`, it represents the probability of observing the data `D` given the parameter `θ`. It reflects how well the parameter `θ` explains the observed data.

3. Posterior Probability (Posterior): Denoted as `P(θ∣D)`, it is the updated probability of the parameter
`θ `after observing the data `D`. It combines the prior probability and the likelihood.


## Stochastic Program

Joint distribution of latent variables and data.

$$
\Pr(\theta, y) = \Pr(y \mid \theta) \Pr(\theta)
$$


## Prior Distribution

Quantifies the uncertainty in latent variables


## Likelihood Function

Conditions our model on the observed data

## Conjugacy

Refers to a situation where the posterior distribution of a parameter, given a prior distribution and the likelihood of observed data, is in the same family as the prior distribution.


## Uncommon terminology common in Probabilistic Programming

- Stochastic: used to describe processes, systems, or variables that are inherently random or probabilistic in nature. In contrast to deterministic processes, where outcomes are precisely determined by initial conditions, stochastic processes involve some level of unpredictability and randomness

- Stochastic vs. Deterministic: In deterministic models, the outcome is fully determined by the initial conditions and the system's rules. In stochastic models, even with known initial conditions and rules, the outcome is not certain and can vary due to random influences.

## ESL

- Latent: Present but not visible, apparent, or activated; existing as potential. something which is hidden and not obvious at the moment, but which may develop further in the future
