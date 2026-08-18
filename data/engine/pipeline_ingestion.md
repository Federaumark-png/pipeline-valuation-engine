# Automatic Pipeline Ingestion Logic

This document describes how the Pipeline Valuation Engine automatically ingests and validates input data.

---

## 1. Files to Ingest

The engine automatically loads:

- `data/pipeline.json`
- `data/company_profile.json`
- `data/drug_database.json`
- `models/config.json`

---

## 2. Ingestion Steps

For each file:

1. Check if the file exists.
2. Load JSON content.
3. Validate required fields.
4. Validate numeric ranges (no negative market size, no >100% probabilities, etc.).
5. Map fields into internal data structures.

---

## 3. Pipeline Validation

The engine validates:

- each drug has: name, indication, phase, market_size, market_share, factor
- phase is one of: Phase 1, Phase 2, Phase 3, Approval
- market_size > 0
- 0% ≤ market_share ≤ 100%
- factor ≥ 1

Invalid entries are:

- flagged in a validation report
- excluded from valuation until fixed

---

## 4. Company Profile Usage

From `company_profile.json`, the engine uses:

- company_name
- headquarters
- therapeutic_focus
- key_partnerships
- revenue
- R&D spend
- strategic strengths and risks

This is injected into the memo’s **Company Overview** section.

---

## 5. Drug Database Cross-Check

The engine cross-checks pipeline drugs against `drug_database.json`:

- matches by name or indication
- uses market_size and competition_level as reference
- adjusts assumptions if needed

---

## 6. Output of Ingestion

The ingestion step produces:

- a clean internal pipeline model
- a validation summary
- warnings for missing or inconsistent data

This is the foundation for all subsequent valuation steps.
