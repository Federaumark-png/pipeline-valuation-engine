# Pipeline Valuation Engine – Healthcare Investment Toolkit

This project provides a risk-adjusted valuation framework for pharmaceutical and biotech pipelines.  
It combines clinical development data, market assumptions, and probability-of-success models to estimate the expected commercial value of drug candidates.

## Current Status (Phase 1)
- `valuation.py`: Core valuation engine
- `pipeline.json`: Example pipeline (BioNTech)
- Risk-adjusted revenue model implemented
- Ready for remote execution on VPS

## Upcoming Features (Phase 2)
- Pipeline Analyzer (FDA + ClinicalTrials.gov integration)
- Healthcare Stock Screener (Yahoo Finance API)
- Sensitivity Analysis (market size, probability, pricing)
- Portfolio Valuation (multi-asset analysis)
- Investment Memo Generator (AI-powered)
- Hermes Agent Integration (tool actions + API endpoints)

  ## AI Agent (Hermes-ready)

This project includes an AI Healthcare Investment Agent:

- `Agents/prompt.txt` – defines the analyst role, workflow, and tone
- `Agents/memo_template.md` – structure for investment memos
- `Agents/actions.py` – Python actions to run valuation, pipeline analysis, stock screening, and memo generation
- `Agents/agent.json` – configuration file describing the agent, its actions, and permissions

The agent is designed to:
- Analyze biotech pipelines from `pipeline.json`
- Perform risk-adjusted valuation using `valuation.py`
- Screen healthcare stocks via `stock_screener.py`
- Generate investment memos using `memo_generator.py`


## Objective
Build a complete Healthcare Investment Toolkit for:
- Investment Banking
- Equity Research
- Pharma Strategy
- Consulting
- Venture Capital

## Why This Project Matters
Pharma and biotech valuation is driven by:
- Clinical development risk
- Market size and pricing assumptions
- Competitive landscape
- Regulatory outcomes
- Probability-adjusted revenue

This engine aims to simplify and standardize these components into a transparent, modular valuation workflow.


