# Memo Generation Engine

This document explains how the Pipeline Valuation Engine combines all logic files to generate a complete investment memo.

---

## 1. Load All Input Files

The engine loads:

- pipeline.json  
- config.json  
- valuation.md  
- multi_valuation.md  
- risk_scoring.md  
- sensitivity.md  
- portfolio_insights.md  
- global_summary.md  
- memo_template.md  
- agent prompt  

---

## 2. Execute Valuation Pipeline

### Step-by-step:

1. Parse pipeline data  
2. Apply success probabilities  
3. Compute expected revenue  
4. Compute base valuation  
5. Apply risk modifiers  
6. Compute adjusted valuation  
7. Run sensitivity analysis  
8. Generate portfolio insights  
9. Generate global summary  

---

## 3. Memo Assembly

The engine fills the memo template with:

- Executive summary  
- Pipeline overview  
- Asset-by-asset valuation  
- Risk assessment  
- Sensitivity analysis  
- Portfolio insights  
- Global valuation summary  
- Final recommendation  

---

## 4. Output Format

The final memo is produced in:

- Markdown  
- Structured sections  
- Analyst-level tone  
- International finance style  

---

## 5. Hermes Integration

Hermes can:

- load all files  
- run the valuation logic  
- generate the memo  
- return the final output automatically  

This makes the system fully autonomous.
