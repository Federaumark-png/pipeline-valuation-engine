from valuation import ValuationEngine
from pipeline_analyzer import PipelineAnalyzer
from stock_screener import HealthcareStockScreener
import json

def main():
    # 1) Load and value pipeline
    ve = ValuationEngine(pipeline_file="pipeline.json", discount_rate=0.12)
    portfolio_result = ve.value_portfolio()

    print("=== PIPELINE VALUATION ===")
    for d in portfolio_result["drugs"]:
        print(f"- {d['name']}:")
        print(f"  Phase: {d['phase']}")
        print(f"  PoS: {d['probability_of_success']:.2f}")
        print(f"  Base NPV: {d['base_npv']:.0f}")
        print(f"  Risk-adjusted NPV: {d['risk_adjusted_npv']:.0f}")
    print(f"Total portfolio risk-adjusted NPV: {portfolio_result['portfolio_risk_adjusted_npv']:.0f}")
    print()

    # 2) Analyze pipeline (FDA + trials)
    pa = PipelineAnalyzer(pipeline_file="pipeline.json")
    analysis = pa.analyze()

    print("=== PIPELINE ANALYSIS (FDA + ClinicalTrials) ===")
    for entry in analysis:
        print(f"- {entry['drug']}:")
        print(f"  Phase: {entry['phase']}")
        print(f"  PoS: {entry['probability_of_success']:.2f}")
        print(f"  FDA data present: {entry['fda_data'] is not None}")
        print(f"  Clinical trials present: {entry['clinical_trials'] is not None}")
    print()

    # 3) Screen healthcare stocks
    screener = HealthcareStockScreener()
    stocks = screener.screen()

    print("=== HEALTHCARE STOCK SCREENER ===")
    for s in stocks:
        if "error" in s:
            print(f"- {s['ticker']}: ERROR {s['error']}")
            continue
        print(f"- {s['ticker']} ({s.get('name')}):")
        print(f"  Market cap: {s.get('market_cap')}")
        print(f"  Revenue: {s.get('revenue')}")
        print(f"  R&D: {s.get('r_and_d')}")
        print(f"  Gross margin: {s.get('gross_margin')}")
        print(f"  Profit margin: {s.get('profit_margin')}")
    print()

if __name__ == "__main__":
    main()
