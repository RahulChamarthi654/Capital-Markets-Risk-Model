"""
Cost of Capital & Equity Risk Analysis Model
--------------------------------------------

This script estimates key capital market metrics used in corporate finance:

- CAGR (long-term growth rate)
- Annualized volatility
- Beta (systematic risk)
- Sharpe ratio (risk-adjusted return)
- CAPM expected return (cost of equity)
- Maximum drawdown (downside risk)

Applications:
- WACC estimation
- Capital budgeting
- Equity valuation
- Strategic capital allocation

Author: Rahul Chamarthi
"""

# --------------------------------------------------
# Import Required Libraries
# --------------------------------------------------

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# Configuration Parameters
# --------------------------------------------------

TICKERS = ["GOOG", "AAPL", "NVDA"]
MARKET_TICKER = "^GSPC"      # S&P 500
RISK_FREE_RATE = 0.04        # 4% annual risk-free rate
PERIOD = "10y"
TRADING_DAYS = 252


# --------------------------------------------------
# Download Historical Data
# --------------------------------------------------

def download_data(ticker):
    """
    Downloads historical data and calculates daily returns.
    """
    data = yf.download(ticker, period=PERIOD, auto_adjust=True)
    data["Daily Return"] = data["Close"].pct_change()
    return data.dropna()


# --------------------------------------------------
# CAGR
# --------------------------------------------------

def calculate_cagr(data):
    years = (data.index[-1] - data.index[0]).days / 365.25
    beginning = data["Close"].iloc[0]
    ending = data["Close"].iloc[-1]
    cagr = (ending / beginning) ** (1 / years) - 1
    return float(cagr)


# --------------------------------------------------
# Annualized Volatility
# --------------------------------------------------

def calculate_annual_volatility(data):
    volatility = data["Daily Return"].std() * np.sqrt(TRADING_DAYS)
    return float(volatility)


# --------------------------------------------------
# Beta
# --------------------------------------------------

def calculate_beta(stock_returns, market_returns):
    combined = pd.concat([stock_returns, market_returns], axis=1).dropna()
    combined.columns = ["Stock", "Market"]

    covariance = combined["Stock"].cov(combined["Market"])
    market_variance = combined["Market"].var()

    beta = covariance / market_variance
    return float(beta)


# --------------------------------------------------
# Sharpe Ratio
# --------------------------------------------------

def calculate_sharpe_ratio(data):
    daily_rf = RISK_FREE_RATE / TRADING_DAYS
    excess_returns = data["Daily Return"] - daily_rf

    annual_excess_return = excess_returns.mean() * TRADING_DAYS
    annual_volatility = calculate_annual_volatility(data)

    sharpe_ratio = annual_excess_return / annual_volatility
    return float(sharpe_ratio)


# --------------------------------------------------
# Maximum Drawdown
# --------------------------------------------------

def calculate_max_drawdown(data):
    cumulative = (1 + data["Daily Return"]).cumprod()
    rolling_max = cumulative.cummax()
    drawdown = cumulative / rolling_max - 1

    return float(drawdown.min()), cumulative


# --------------------------------------------------
# CAPM Expected Return (Cost of Equity)
# --------------------------------------------------

def calculate_capm_return(beta, market_returns):
    market_annual_return = market_returns.mean() * TRADING_DAYS
    capm_return = RISK_FREE_RATE + beta * (market_annual_return - RISK_FREE_RATE)
    return float(capm_return)


# --------------------------------------------------
# Main Execution
# --------------------------------------------------

def main():

    results = {}

    # Download market data
    market_data = download_data(MARKET_TICKER)
    market_returns = market_data["Daily Return"]

    for ticker in TICKERS:

        stock_data = download_data(ticker)

        cagr = calculate_cagr(stock_data)
        volatility = calculate_annual_volatility(stock_data)
        beta = calculate_beta(stock_data["Daily Return"], market_returns)
        sharpe = calculate_sharpe_ratio(stock_data)
        max_dd, cumulative = calculate_max_drawdown(stock_data)
        capm = calculate_capm_return(beta, market_returns)

        results[ticker] = {
            "CAGR": cagr,
            "Volatility": volatility,
            "Beta": beta,
            "Sharpe Ratio": sharpe,
            "Cost of Equity (CAPM)": capm,
            "Max Drawdown": max_dd,
            "Cumulative Returns": cumulative
        }

    # --------------------------------------------------
    # Create Summary Table
    # --------------------------------------------------

    summary = pd.DataFrame(results).T
    summary = summary[[
        "CAGR",
        "Volatility",
        "Beta",
        "Sharpe Ratio",
        "Cost of Equity (CAPM)",
        "Max Drawdown"
    ]]

    summary = summary.sort_values(by="Sharpe Ratio", ascending=False)

    print("\n===== Capital Markets Risk Summary =====\n")

    # --------------------------------------------------
    # Professional Formatting for Terminal Output
    # --------------------------------------------------

    formatted_summary = summary.copy()

    def format_percent(x):
        return f"{x:.2%}"

    def format_float(x):
        return f"{x:.2f}"

    formatted_summary["CAGR"] = formatted_summary["CAGR"].apply(format_percent)
    formatted_summary["Volatility"] = formatted_summary["Volatility"].apply(format_percent)
    formatted_summary["Beta"] = formatted_summary["Beta"].apply(format_float)
    formatted_summary["Sharpe Ratio"] = formatted_summary["Sharpe Ratio"].apply(format_float)
    formatted_summary["Cost of Equity (CAPM)"] = formatted_summary["Cost of Equity (CAPM)"].apply(format_percent)
    formatted_summary["Max Drawdown"] = formatted_summary["Max Drawdown"].apply(format_percent)

    print(formatted_summary.to_string())

    # --------------------------------------------------
    # Risk vs Return Visualization
    # --------------------------------------------------

    plt.figure(figsize=(10, 6))

    for ticker in TICKERS:
        plt.scatter(
            results[ticker]["Volatility"],
            results[ticker]["CAGR"],
            s=120,
            label=ticker
        )

    plt.title("Risk vs Return (CAGR vs Volatility)")
    plt.xlabel("Annualized Volatility")
    plt.ylabel("Compound Annual Growth Rate (CAGR)")
    plt.grid(True)
    plt.legend()

    # Format axes as percentages
    plt.gca().xaxis.set_major_formatter(lambda x, _: f"{x:.0%}")
    plt.gca().yaxis.set_major_formatter(lambda y, _: f"{y:.0%}")

    plt.show()


# --------------------------------------------------
# Run Program
# --------------------------------------------------

if __name__ == "__main__":
    main()