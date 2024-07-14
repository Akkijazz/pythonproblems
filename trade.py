import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Function to fetch historical data for a given stock ticker
def fetch_data(ticker, start, end):
    stock_data = yf.download(ticker, start=start, end=end)
    return stock_data


# Function to identify support and resistance levels
def identify_levels(data, window=20):
    data["HighMax"] = data["High"].rolling(window=window).max()
    data["LowMin"] = data["Low"].rolling(window=window).min()
    data["VolumeMA"] = (
        data["Volume"].rolling(window=window).mean()
    )  # Adding moving average of volume
    return data


# Function to plot the data with breakout signals
def plot_breakouts(data, ticker):
    plt.figure(figsize=(14, 7))
    plt.plot(data["Close"], label=f"{ticker} Close Price")
    plt.plot(data["HighMax"], label="Resistance Level", linestyle="--")
    plt.plot(data["LowMin"], label="Support Level", linestyle="--")

    for i in range(1, len(data)):
        if (
            data["Close"][i] > data["HighMax"][i - 1]
            and data["Volume"][i] > data["VolumeMA"][i]
        ):  # Buy signal with volume confirmation
            plt.plot(data.index[i], data["Close"][i], marker="^", color="g")
        elif (
            data["Close"][i] < data["LowMin"][i - 1]
            and data["Volume"][i] > data["VolumeMA"][i]
        ):  # Sell signal with volume confirmation
            plt.plot(data.index[i], data["Close"][i], marker="v", color="r")

    plt.title(f"{ticker} Breakout Trading")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()


# Function to simulate trades based on breakout signals
def simulate_trades(data, ticker):
    trades = []
    for i in range(1, len(data)):
        if (
            data["Close"][i] > data["HighMax"][i - 1]
            and data["Volume"][i] > data["VolumeMA"][i]
        ):  # Buy signal
            entry_price = data["Close"][i]
            stop_loss = data["LowMin"][i - 1]
            target_price = (
                entry_price + (entry_price - stop_loss) * 2
            )  # Example of 1:2 risk-reward ratio
            trades.append(("Buy", data.index[i], entry_price, stop_loss, target_price))
        elif (
            data["Close"][i] < data["LowMin"][i - 1]
            and data["Volume"][i] > data["VolumeMA"][i]
        ):  # Sell signal
            entry_price = data["Close"][i]
            stop_loss = data["HighMax"][i - 1]
            target_price = (
                entry_price - (stop_loss - entry_price) * 2
            )  # Example of 1:2 risk-reward ratio
            trades.append(("Sell", data.index[i], entry_price, stop_loss, target_price))
    return trades


# Parameters for the trading setup
ticker = "TCS"  # Example stock ticker (Apple Inc.)
start_date = "2022-01-01"  # Start date for historical data
end_date = "2023-01-01"  # End date for historical data
window_size = 20  # Window size for rolling calculations

# Fetch and process data
data = fetch_data(ticker, start=start_date, end=end_date)
data = identify_levels(data, window=window_size)

# Plot the breakout signals
plot_breakouts(data, ticker)

# Simulate trades and print results
trades = simulate_trades(data, ticker)
for trade in trades:
    print(trade)
