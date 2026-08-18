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
For each parameter variation:

1. The engine selects one parameter to vary (market share, probability, factor, or risk).
2. It applies the variant value (low/base/high).
3. It recalculates expected revenue using the new market share and probability.
4. It recalculates valuation using the new valuation factor.
5. It applies the corresponding risk modifier variant (downside/base/upside).
6. It computes the adjusted valuation.
7. It stores the result in the sensitivity table.

---

## 6. Full Sensitivity Workflow

The complete workflow for each scenario is:

### Low Case Scenario
- market_share = 10%  
- success_probability = base_probability − 10%  
- valuation_factor = 3×  
- risk_modifier = downside  
- adjusted_valuation = recomputed low-case value  

### Base Case Scenario
- market_share = 20%  
- success_probability = base_probability  
- valuation_factor = 4×  
- risk_modifier = base  
- adjusted_valuation = recomputed base-case value  

### High Case Scenario
- market_share = 30%  
- success_probability = base_probability + 10%  
- valuation_factor = 5×  
- risk_modifier = upside  
- adjusted_valuation = recomputed high-case value  

---

## 7. Sensitivity Output Usage

The sensitivity results are used to:

- identify valuation volatility  
- highlight parameters with strongest impact  
- determine upside/downside exposure  
- support final investment recommendation  
- strengthen portfolio-level insights  

The memo integrates these results into the sensitivity section and the global summary.

