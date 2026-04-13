# ==========================================
# AlphaPulse - Main Pipeline
# ==========================================

from src.data_loader import load_data
from src.preprocessing import clean_data
from src.analysis import (
    calculate_returns,
    calculate_volatility,
    calculate_correlation
)
from src.simulation import monte_carlo_simulation

import numpy as np
import pandas as pd
import os

# ------------------------------------------
# CONFIG
# ------------------------------------------

stocks = ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'AMZN']
start_date = "2020-01-01"
end_date = "2024-01-01"

output_path = "data/processed"
os.makedirs(output_path, exist_ok=True)

# ------------------------------------------
# STEP 1: LOAD DATA
# ------------------------------------------

print("Loading data...")
data = load_data(stocks, start_date, end_date)

# Save raw data
data.to_csv("data/raw/stock_prices_raw.csv")

# ------------------------------------------
# STEP 2: CLEAN DATA
# ------------------------------------------

print("Cleaning data...")
data = clean_data(data)

data.to_csv(f"{output_path}/stock_prices_clean.csv")

# ------------------------------------------
# STEP 3: ANALYSIS
# ------------------------------------------

print("Performing analysis...")

returns = calculate_returns(data)
volatility = calculate_volatility(returns)
correlation = calculate_correlation(returns)

returns.to_csv(f"{output_path}/returns.csv")
volatility.to_csv(f"{output_path}/rolling_volatility.csv")
correlation.to_csv(f"{output_path}/correlation_matrix.csv")

# ------------------------------------------
# STEP 4: PORTFOLIO
# ------------------------------------------

print("Calculating portfolio metrics...")

weights = np.array([1 / len(stocks)] * len(stocks))

portfolio_returns = returns.dot(weights)
portfolio_returns.to_csv(f"{output_path}/portfolio_returns.csv")

# ------------------------------------------
# STEP 5: MONTE CARLO SIMULATION
# ------------------------------------------

print("Running Monte Carlo simulation...")

sim_df = monte_carlo_simulation(returns)
sim_df.to_csv(f"{output_path}/monte_carlo.csv", index=False)

# ------------------------------------------
# STEP 6: VALUE AT RISK (VaR)
# ------------------------------------------

print("Calculating VaR...")

VaR_95 = np.percentile(portfolio_returns, 5)

var_df = pd.DataFrame({"VaR_95": [VaR_95]})
var_df.to_csv(f"{output_path}/var.csv", index=False)

# ------------------------------------------
# DONE
# ------------------------------------------

print("\nPipeline completed successfully!")
print(f"All files saved in: {output_path}")
