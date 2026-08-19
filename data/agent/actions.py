from valuation import ValuationEngine
from pipeline_analyzer import PipelineAnalyzer
from stock_screener import HealthcareStockScreener
from memo_generator import generate_memo

# Hermes Action: Run pipeline valuation
def action_run_valuation():
    ve = ValuationEngine("pipeline.json")
    return ve.value_portfolio()

# Hermes Action: Run pipeline analyzer
def action_run_pipeline_analysis():
    pa = PipelineAnalyzer("pipeline.json")
    return pa.analyze()

# Hermes Action: Run stock screener
def action_run_stock_screener():
    screener = HealthcareStockScreener()
    return screener.screen()

# Hermes Action: Generate investment memo
def action_generate_memo():
    memo = generate_memo()
    return memo
