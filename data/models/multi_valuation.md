# Multi-Drug Valuation Logic

This document explains how the Pipeline Valuation Engine calculates the total valuation across multiple assets.

---

## 1. Individual Asset Valuation
Each drug is valued independently using:

- Market size  
- Market share  
- Price per treatment  
- Success probability  
- Valuation factor  
- Risk adjustments  

Formula:
expected_revenue = (market_size × market_share) × success_probability
valuation = expected_revenue × valuation_factor

---

## 2. Risk Adjustments
Risk modifiers from `config.json` are applied:

Positive:
- strong_ip → +10%
- breakthrough_designation → +15%

Negative:
- high_competition → -15%
- regulatory_risk → -10%
- manufacturing_risk → -5%

Adjusted valuation:
