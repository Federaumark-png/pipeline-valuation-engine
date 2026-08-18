# Hermes Integration Guide

This document explains how to integrate the Pipeline Valuation Engine with a Hermes AI agent.

---

## 1. Required Files

Hermes must load the following files:

### Data
- `data/pipeline.json`
- `data/company_profile.json`
- `data/drug_database.json`

### Models
- `models/valuation.md`
- `models/multi_valuation.md`
- `models/risk_scoring.md`
- `models/sensitivity.md`
- `models/portfolio_insights.md`
- `models/global_summary.md`
- `models/valuation_examples.md`
- `models/config.json`

### Agent
- `agent/prompt_advanced.txt`
- `agent/memo_template.md`

### Engine
- `engine/memo_generation.md`

---

## 2. Loading Files in Hermes

Hermes can load files using:

- RAW GitHub URLs  
- Local paths  
- Workspace files  

https://raw.githubusercontent.com/<username>/<repo>/main/data/pipeline.json

Hermes should load all files before generating the memo.

---

## 3. Running the Valuation Pipeline

Hermes performs:

1. Parse pipeline data  
2. Apply success probabilities  
3. Compute expected revenue  
4. Compute base valuation  
5. Apply risk modifiers  
6. Compute adjusted valuation  
7. Run sensitivity analysis  
8. Generate portfolio insights  
9. Generate global summary  
10. Assemble memo using template  

---

## 4. Generating the Memo

Hermes produces a complete memo containing:

- Executive summary  
- Pipeline overview  
- Asset valuations  
- Risk assessment  
- Sensitivity analysis  
- Portfolio insights  
- Global summary  
- Final recommendation  

---

## 5. Example Hermes Command

Generate a full investment memo using all project files.

Hermes will automatically:

- load all files  
- run all logic  
- produce the memo  

---

## 6. Output Format

Hermes returns:

- Markdown memo  
- Analyst-level tone  
- International finance style  

Example RAW URL:

