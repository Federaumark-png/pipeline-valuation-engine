# Global Valuation Summary Logic

This document explains how the Pipeline Valuation Engine produces a global summary across all valuation components.

---

## 1. Total Expected Revenue
The system aggregates expected revenue from all assets:

total_expected_revenue

This represents the combined commercial potential of the pipeline.

---

## 2. Total Valuation (Base Case)
The system sums all base-case valuations:

 = Σ expected_revenue(drug_i)
 total_valuation = Σ valuation(drug_i)
This is the unadjusted pipeline value.

---

## 3. Total Risk-Adjusted Valuation
Risk modifiers are applied to each asset, then aggregated:

total_risk_adjusted_valuation = Σ adjusted_valuation(drug_i)

This represents the realistic valuation after risk exposure.

---

## 4. Upside vs Downside
The system compares:

- **Upside scenario** (high market share, high probability, high factor)
- **Base scenario**
- **Downside scenario** (low market share, low probability, low factor)

Output includes:

- upside potential  
- downside protection  
- valuation volatility  

---

## 5. Portfolio Stability Score
The system evaluates:

- diversification across phases  
- diversification across therapeutic areas  
- risk concentration  
- sensitivity concentration  

Score ranges:

- **Stable portfolio** → diversified, low volatility  
- **Moderate stability** → mixed risk distribution  
- **High volatility** → concentrated risk, high sensitivity  

---

## 6. Final Investment Stance
The memo concludes with:

- Buy / Hold / Avoid  
- Rationale  
- Key upside drivers  
- Key downside risks  
- Strategic implications  

---

## 7. Output Integration
The global summary is included in:

- Executive summary  
- Total valuation section  
- Portfolio insights  
- Final recommendation  
