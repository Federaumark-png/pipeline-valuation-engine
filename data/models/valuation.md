# Valuation Logic (Explanation)

This document explains the valuation logic used by the Pipeline Valuation Engine.

---

## 1. Success Probabilities

- Phase 1 → 10%  
- Phase 2 → 30%  
- Phase 3 → 60%  
- Approval → 100%

---

## 2. Revenue Formula

revenue = market_size × market_share

Example:  
€3,000,000,000 × 20% = €600,000,000

---

## 3. Expected Revenue

expected_revenue = revenue × success_probability


Example:  
€600,000,000 × 30% = €180,000,000

---

## 4. Valuation Factor

valuation = expected_revenue × factor

Example:  
€180,000,000 × 4 = €720,000,000


