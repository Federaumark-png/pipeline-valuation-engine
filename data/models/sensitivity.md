# Sensitivity Analysis Logic

This document explains how the Pipeline Valuation Engine performs sensitivity analysis on key valuation parameters.

---

## 1. Parameters Tested

The system evaluates how changes in the following parameters affect valuation:

### Market Share
- Low case: 10%
- Base case: 20%
- High case: 30%

### Success Probability
- -10% deviation
- Base probability
- +10% deviation

### Valuation Factor
- Conservative: 3×
- Base: 4×
- Optimistic: 5×

### Risk Modifiers
- Removing negative risks
- Removing positive risks
- Applying extreme downside
- Applying extreme upside

---

## 2. Sensitivity Formula
expected_revenue = (market_size × market_share_variant) × success_probability_variant
valuation = expected_revenue × valuation_factor_variant
adjusted_valuation = valuation × (1 + total_risk_modifier_variant)
---

## 3. Output Table

The system generates a sensitivity table:

| Scenario | Market Share | Success Prob. | Factor | Risk Adj. | Valuation |
|---------|--------------|---------------|--------|-----------|-----------|
| Low Case | 10% | -10% | 3× | downside | lower valuation |
| Base Case | 20% | base | 4× | base | base valuation |
| High Case | 30% | +10% | 5× | upside | higher valuation |

---

## 4. Interpretation

The memo includes:

- Key drivers of upside  
- Key drivers of downside  
- Most sensitive parameter  
- Least sensitive parameter  
- Strategic implications  

---

## 5. Why Sensitivity Matters

Sensitivity analysis helps investors understand:

- valuation stability  
- risk exposure  
- upside potential  
- downside protection  

For each parameter variation:

