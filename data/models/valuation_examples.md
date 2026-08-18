# Valuation Math Examples

This document provides concrete numerical examples to illustrate how the Pipeline Valuation Engine performs calculations.

---

## 1. Base Valuation Example

Drug:
- Market size: €3,000,000,000  
- Market share: 20%  
- Success probability (Phase 2): 30%  
- Valuation factor: 4×

### Step 1 — Revenue

revenue = market_size × market_share
revenue = 3,000,000,000 × 0.20 = 600,000,000

### Step 2 — Expected Revenue
expected_revenue = revenue × success_probability
expected_revenue = 600,000,000 × 0.30 = 180,000,000

### Step 3 — Valuation
valuation = expected_revenue × factor
valuation = 180,000,000 × 4 = 720,000,000

---

## 2. Risk-Adjusted Example

Risk modifiers:
- regulatory_risk: -10%  
- high_competition: -15%  
- strong_ip: +10%  

### Combined Risk
total_risk_modifier = -0.10 - 0.15 + 0.10 = -0.15

### Adjusted Valuation
adjusted_valuation = valuation × (1 + total_risk_modifier)
adjusted_valuation = 720,000,000 × 0.85 = 612,000,000

---

## 3. Sensitivity Example

### Low Case
- Market share: 10%  
- Probability: -10%  
- Factor: 3×  

### High Case
- Market share: 30%  
- Probability: +10%  
- Factor: 5×  

The memo will show:
- downside valuation  
- base valuation  
- upside valuation  

---

## 4. Portfolio Example

If three drugs have adjusted valuations:

- Drug A: €612M  
- Drug B: €1.2B  
- Drug C: €450M  

### Total Pipeline Value
total_pipeline_value = 612M + 1.2B + 450M = 2.262B


---

## 5. Global Summary Example

The memo will include:

- total expected revenue  
- total valuation  
- total risk-adjusted valuation  
- upside/downside comparison  
- stability score  
