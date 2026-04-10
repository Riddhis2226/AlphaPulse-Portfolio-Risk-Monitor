import numpy as np
import pandas as pd

def monte_carlo_simulation(returns, num_simulations=10000, num_days=252):
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    num_assets = len(mean_returns)

    results = []

    for _ in range(num_simulations):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)

        portfolio_return = np.sum(mean_returns * weights) * num_days
        portfolio_std = np.sqrt(
            np.dot(weights.T, np.dot(cov_matrix, weights))
        ) * np.sqrt(num_days)

        results.append([portfolio_return, portfolio_std])

    return pd.DataFrame(results, columns=['Returns', 'Volatility'])
