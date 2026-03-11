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

## Applications in Corporate Finance

This model can be applied in areas such as:

- Cost of capital (WACC) estimation  
- Equity valuation models  
- Capital budgeting decisions  
- Strategic capital allocation analysis  
- Risk assessment and performance benchmarking  

---

## Technologies Used (Displayed in requirements.txt)

- Python  
- pandas  
- NumPy  
- matplotlib  
- yfinance  

---

## Installation (Local Environment)

### 1. Clone the repository

```
git clone https://github.com/RahulChamarthi654/Capital-Markets-Risk-Model.git
```

### 2. Navigate to the project folder

```
cd Capital-Markets-Risk-Model
```

### 3. Install required libraries

```
pip install -r requirements.txt
```

---

## Running the Program

After installing libraries and dependencies, run the script:

```
python main.py
```

The program will:

1. Download historical market data  
2. Calculate risk and return metrics  
3. Print a formatted summary table in the terminal  
4. Display a Risk vs. Return visualization  

---

## Running in Google Colab

This project can also be run directly in Google Colab without installing any dependencies.


---

## Example Output (Image included in repository)

The program produces:

- A formatted **capital markets risk summary table**
- A **Risk vs. Return scatter plot** comparing equities by volatility and CAGR

---
## Author

Rahul Chamarthi
