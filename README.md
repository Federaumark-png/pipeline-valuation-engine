# Pipeline Valuation Engine

The Pipeline Valuation Engine is a structured AI project that automates the valuation of biotech and pharma pipelines.  
It combines data, valuation logic, and an AI agent to generate a professional investment memo.

---

## 📁 Project Structure


---

## 🔍 How It Works

1. **Load pipeline data**  
   The system reads the pipeline from `data/pipeline.json`.

2. **Identify clinical phase**  
   The agent identifies the phase (Phase 1, Phase 2, Phase 3, Approval).

3. **Apply success probability**  
   - Phase 1 → 10%  
   - Phase 2 → 30%  
   - Phase 3 → 60%  
   - Approval → 100%

4. **Calculate revenue**  
   `Revenue = market_size × market_share`

5. **Calculate expected revenue**  
   `Expected revenue = revenue × success_probability`

6. **Calculate pipeline valuation**  
   `Valuation = expected_revenue × factor`

---

## 🧠 AI Agent

The agent in `agent/prompt.txt` generates a full investment memo:

- Summary  
- Pipeline description  
- Valuation  
- Risks  
- Recommendation  

---

## 🌐 Optional: Hermes Agent Integration

Files can later be loaded into a Hermes agent using RAW URLs or local paths.

Example RAW URL:
`https://raw.githubusercontent.com/<username>/pipeline-valuation-engine/main/data/pipeline.json`

---

## 🎯 Project Goal

This project demonstrates:

- Understanding of pharma pipeline valuation  
- Structured AI project design  
- Clean separation of data, logic, and agent  
- Professional documentation  


