import numpy as np

def calculate_returns(data):
    return np.log(data / data.shift(1)).dropna()

def calculate_volatility(returns):
    return returns.rolling(window=30).std()

def calculate_correlation(returns):
    return returns.corr()
