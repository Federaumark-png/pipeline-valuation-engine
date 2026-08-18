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
adjusted_valuation = valuation × (1 + total_risk_modifier)

---

## 3. Total Pipeline Valuation
All adjusted valuations are summed:
total_pipeline_value = Σ adjusted_valuation(drug_i)


---

## 4. Portfolio Insights
The system also generates:

- Top-value asset  
- Highest-risk asset  
- Most sensitive asset  
- Combined expected revenue  
- Combined valuation  
- Key drivers  
- Key downside factors  

---

## 5. Output
The final memo uses this logic to produce:

- Executive summary  
- Asset-by-asset breakdown  
- Total valuation  
- Risk assessment  
- Recommendation  


