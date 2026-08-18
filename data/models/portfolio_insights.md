# Portfolio Insights Logic

This document explains how the Pipeline Valuation Engine generates portfolio-level insights across all assets.

---

## 1. Top-Value Asset
The system identifies the drug with the highest adjusted valuation.

Criteria:
- highest expected revenue  
- strongest upside  
- lowest negative risk impact  

---

## 2. Highest-Risk Asset
The system identifies the drug with the strongest negative risk modifiers.

Criteria:
- regulatory risk  
- competition  
- manufacturing complexity  

Insight:
This asset contributes most to downside volatility.

---

## 3. Most Sensitive Asset
The system determines which drug changes the most under sensitivity analysis.

Criteria:
- valuation factor variation  
- market share variation  
- probability variation  

Insight:
This asset drives overall portfolio uncertainty.

---

## 4. Combined Portfolio Strength
The system evaluates:

- total pipeline valuation  
- diversification across phases  
- diversification across therapeutic areas  
- risk concentration  
- upside concentration  

---

## 5. Strategic Implications
The memo includes:

- which assets should be prioritized  
- which assets need derisking  
- which assets have the strongest commercial potential  
- which assets drive long-term value  

---

## 6. Output
The final memo integrates portfolio insights into:

- Executive summary  
- Asset ranking  
- Risk distribution  
- Sensitivity highlights  
- Final recommendation  
