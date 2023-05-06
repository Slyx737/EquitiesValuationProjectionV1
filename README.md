# Equity Valuation Projections 

Equity Valuation Projections (EquityValuationProjections) is a Python script that provides a template for projecting the future share price of a company based on historical revenue, earnings growth, dilution, and industry-average valuations. The algorithm calculates projected revenue, earnings per share (EPS), net income, enterprise value, and future share price, offering insights into potential investment opportunities.

## Overview

Investors often seek to understand the potential future value of a company's shares based on its historical financial performance and industry trends. EquityValuationProjections is designed to assist in this analysis by providing a simplified model for projecting a company's future share price.

The algorithm takes into account the following inputs:
- Historical revenue
- Historical earnings per share (EPS)
- Shares outstanding
- Industry-average price-to-earnings (P/E) ratio
- Dilution rate
- Number of years into the future for the projection

Based on these inputs, the algorithm calculates the following projections:
- Projected revenue
- Projected EPS
- Projected net income
- Projected enterprise value
- Projected share price

## Usage

To use EquityValuationProjections, modify the input values in the script to match the specific company you want to analyze. The input values include historical revenue, historical EPS, shares outstanding, industry-average P/E ratio, dilution rate, and the number of years into the future for the projection.

The script will then calculate and output the projected share price for the specified number of years into the future.

```python
# Example usage
historical_revenue = [565.53, 977.30, 1520, 1980]  # in millions
historical_eps = [-4.30, -1.00, -0.40]  # GAAP EPS
shares_outstanding = 941.68  # in millions
industry_pe_ratio = 20
dilution_rate = 0.04
years = 5

projected_price = project_future_share_price(historical_revenue, historical_eps, shares_outstanding, industry_pe_ratio, dilution_rate, years)
print(f"Projected Share Price in {years} Years: ${projected_price:.2f}")
