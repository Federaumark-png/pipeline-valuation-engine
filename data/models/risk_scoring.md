# Risk Scoring Logic

This document explains how the Pipeline Valuation Engine applies risk adjustments to each drug.

---

## 1. Risk Categories

The system evaluates the following risk dimensions:

### Negative risks
- **Regulatory risk**  
  Probability of delays or rejection by authorities.

- **High competition**  
  Strong competitors reduce market share and pricing power.

- **Manufacturing risk**  
  Complexity of production, supply chain issues.

### Positive risks (upside)
- **Strong IP protection**  
  Patents, exclusivity, freedom-to-operate.

- **Breakthrough designation**  
  Faster approval, higher probability of success.

---

## 2. Risk Modifiers (from config.json)

high_competition: -0.15
regulatory_risk: -0.10
manufacturing_risk: -0.05
strong_ip: +0.10
breakthrough_designation: +0.15


---

## 3. Combined Risk Score

Each drug receives a combined risk score:

total_risk_modifier = sum(all applicable risk modifiers)


Example:
- regulatory_risk → -0.10  
- high_competition → -0.15  
- strong_ip → +0.10  

Total:
total_risk_modifier = -0.15

---

## 4. Adjusted Valuation

The risk score modifies the valuation:

adjusted_valuation = valuation × (1 + total_risk_modifier)

Example:
- valuation = 720M  
- total_risk_modifier = -0.15  

Adjusted:
adjusted_valuation = 720M × 0.85 = 612M

---

## 5. Output

The final memo includes:
- risk summary  
- key downside factors  
- key upside factors  
- risk-adjusted valuation  
