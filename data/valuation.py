import json

# --- Load pipeline data ---
with open("data/pipeline.json", "r") as f:
    pipeline = json.load(f)

# --- Success probabilities ---
SUCCESS_PROB = {
    "Phase 1": 0.10,
    "Phase 2": 0.30,
    "Phase 3": 0.60,
    "Approval": 1.00
}

# --- Default assumptions ---
DEFAULT_MARKET_SHARE = 0.20   # 20%
DEFAULT_FACTOR = 4            # valuation multiplier

def valuate_drug(drug):
    market_size = drug["market_size"]
    market_share = DEFAULT_MARKET_SHARE
    factor = DEFAULT_FACTOR
    phase = drug["phase"]

    # 1. Revenue
    revenue = market_size * market_share

    # 2. Expected revenue
    success_prob = SUCCESS_PROB.get(phase, 0)
    expected_revenue = revenue * success_prob

    # 3. Valuation
    valuation = expected_revenue * factor

    return {
        "name": drug["name"],
        "phase": phase,
        "revenue": revenue,
        "expected_revenue": expected_revenue,
        "valuation": valuation
    }

# --- Run valuation for all drugs ---
results = []
for drug in pipeline["drugs"]:
    results.append(valuate_drug(drug))

# --- Print results ---
print(f"Company: {pipeline['company']}\n")
for r in results:
    print(f"Drug: {r['name']}")
    print(f"  Phase: {r['phase']}")
    print(f"  Revenue: {r['revenue']:,}")
    print(f"  Expected Revenue: {r['expected_revenue']:,}")
    print(f"  Valuation: {r['valuation']:,}")
    print()
