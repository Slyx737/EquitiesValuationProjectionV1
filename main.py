def project_future_share_price(historical_revenue, historical_eps, shares_outstanding, industry_pe_ratio, dilution_rate, years):
    # Calculate revenue CAGR
    revenue_cagr = (historical_revenue[-1] / historical_revenue[0]) ** (1 / (len(historical_revenue) - 1)) - 1
    
    # Calculate average rate of improvement in earnings (EPS)
    eps_growth_rates = [(historical_eps[i] - historical_eps[i - 1]) / abs(historical_eps[i - 1]) for i in range(1, len(historical_eps))]
    avg_eps_growth_rate = sum(eps_growth_rates) / len(eps_growth_rates)
    
    # Project future revenue and EPS
    projected_revenue = historical_revenue[-1] * (1 + revenue_cagr) ** years
    projected_eps = historical_eps[-1] * (1 + avg_eps_growth_rate) ** years
    
    # Calculate projected net income
    projected_net_income = projected_eps * shares_outstanding
    
    # Apply industry-average P/E ratio to calculate projected enterprise value
    projected_enterprise_value = projected_net_income * industry_pe_ratio
    
    # Adjust for potential dilution
    adjusted_shares_outstanding = shares_outstanding * (1 + dilution_rate) ** years
    
    # Calculate projected share price
    projected_share_price = projected_enterprise_value / adjusted_shares_outstanding
    
    return projected_share_price

# Example usage
historical_revenue = [565.53, 977.30, 1520, 1980]  # in millions
historical_eps = [-4.30, -1.00, -0.40]  # GAAP EPS
shares_outstanding = 941.68  # in millions
industry_pe_ratio = 20
dilution_rate = 0.04
years = 5

projected_price = project_future_share_price(historical_revenue, historical_eps, shares_outstanding, industry_pe_ratio, dilution_rate, years)
print(f"Projected Share Price in {years} Years: ${projected_price:.2f}")
