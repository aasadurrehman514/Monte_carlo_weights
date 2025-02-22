import numpy as np
from scipy.stats import beta

def generate_random_number():
    return np.random.rand()

def inverse_cdf_beta_dist(event):
    return beta.ppf(generate_random_number(), event['alpha_est'], event['beta_est'])

def run_simulations(event):
    results = dict()
    for i in range(1, event['number_of_simulations'] +1):
        results[i] = inverse_cdf_beta_dist(event)
        
    return results
