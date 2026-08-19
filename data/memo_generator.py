import json
from valuation import ValuationEngine
from pipeline_analyzer import PipelineAnalyzer
from stock_screener import HealthcareStockScreener

def load_template(path="Agents/memo_template.md"):
    with open(path, "r") as f:
        return f.read()

def generate_memo():
    # Load template
    template = load_template()

    # Run valuation
    ve = ValuationEngine("pipeline.json")
    valuation = ve.value_portfolio()

    # Run pipeline analysis
    pa = PipelineAnalyzer("pipeline.json")
    analysis = pa.analyze()

    # Run stock screener
    screener = HealthcareStockScreener()
    stocks = screener.screen()

    # Extract company name from pipeline.json
    with open("pipeline.json", "r") as f:
        pipeline_data = json.load(f)
    company_name = pipeline_data.get("company", "Unknown Company")

    # Build memo content
    memo = template

    memo = memo.replace("Company name", company_name)
    memo = memo.replace("Number of assets", str(len(pipeline_data["drugs"])))

    # Build pipeline overview text
    phases = [d["phase"] for d in pipeline_data["drugs"]]
    memo = memo.replace("Clinical phases", ", ".join(phases))

    # Asset-by-asset section
    asset_section = ""
    for drug in valuation["drugs"]:
        asset_section += f"""
### {drug['name']}
- Phase: {drug['phase']}
- Probability of Success: {drug['probability_of_success']:.2f}
- Risk-adjusted NPV: {drug['risk_adjusted_npv']:.0f}
"""
    memo = memo.replace("For each drug:", asset_section)

    # Total valuation
    memo = memo.replace(
        "Combined valuation",
        str(round(valuation["portfolio_risk_adjusted_npv"], 2))
    )

    return memo

def save_memo(output_path="investment_memo.md"):
    memo = generate_memo()
    with open(output_path, "w") as f:
        f.write(memo)
    print(f"Memo saved to {output_path}")

if __name__ == "__main__":
    save_memo()
