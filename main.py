import argparse
import scipy.stats as stats
import scipy.optimize as opt

from monte_carlo_simulations import run_simulations
from visuals import plot_dist


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--pd_best', type=float, default = 0.0023397)
    parser.add_argument('--pd_base', type=float, default = 0.01013717)
    parser.add_argument('--pd_worst', type=float, default = 0.0348274)
    parser.add_argument('--guess_alpha', type=float, default = 2.0)
    parser.add_argument('--guess_beta', type=float, default = 2.0)
    parser.add_argument('--number_of_simulations', type=int, default = 10000)

    args = parser.parse_args()
    event = vars(args)

    event['alpha_est'], event['beta_est'] = find_alpha_beta(event)
    results = run_simulations(event)
    plot_dist(results)


def find_alpha_beta(event):
    return opt.fsolve(lambda x: beta_params(x, event), [event['guess_alpha'], event['guess_beta']])

def variance_est(event):
    return ((event['pd_worst'] - event['pd_best']) / 4) ** 2

def beta_params(x, event):
    alpha, beta = x
    mean_eq = alpha / (alpha + beta) - event['pd_base']
    var_eq = (alpha * beta) / ((alpha + beta) ** 2 * (alpha + beta + 1)) - variance_est(event)
    return [mean_eq, var_eq]


if __name__ == "__main__":
    main()