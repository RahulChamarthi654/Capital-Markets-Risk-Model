# Capital Markets Risk & Cost of Equity Model

## Overview

This project is a corporate finance model that evaluates publicly traded equities using core capital market risk and return metrics. 

The program analyzes 10 years of historical market data to estimate systematic risk, total risk, downside risk, and the cost of equity under the Capital Asset Pricing Model (CAPM).

In addition to producing a structured summary table, the model generates a Risk vs. Return visualization (CAGR vs. Volatility) to illustrate the relationship between return and total risk across selected equities.

---

## Metrics Calculated

- **Compound Annual Growth Rate (CAGR)** – Long-term annualized return
- **Annualized Volatility** – Total risk (standard deviation of returns)
- **Beta** – Systematic risk relative to the S&P 500
- **Sharpe Ratio** – Risk-adjusted return
- **CAPM Expected Return (Cost of Equity)** – Required return based on systematic risk
- **Maximum Drawdown** – Largest peak-to-trough decline

---

## Visualization

The model produces a **Risk vs. Return scatter plot**, where:

- X-axis = Annualized Volatility  
- Y-axis = Compound Annual Growth Rate (CAGR)  

This visualization demonstrates the fundamental capital markets principle that higher expected returns are generally associated with higher risk.

---

## Applications in Corporate Finance

This model can be used in:

- Cost of capital (WACC) estimation
- Equity valuation models
- Capital budgeting decisions
- Strategic capital allocation analysis
- Risk assessment and performance benchmarking

---

## Technologies Used

- Python
- pandas
- NumPy
- matplotlib
- yfinance

---

