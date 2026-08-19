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
from company_selector import unified_company_selection

def action_find_companies():
    return unified_company_selection()

def action_find_specific_companies(tickers):
    return unified_company_selection(manual_list=tickers)

from auto_pipeline_builder import save_pipeline

def action_auto_pipeline(company_name, ticker=None):
    """
    Automatically generate a pipeline.json for a discovered company.
    """
    output = save_pipeline(company_name, ticker, output="pipeline.json")
    return {
        "status": "success",
        "file": output,
        "company": company_name
    }

def action_manual_pipeline(company_name, ticker=None):
    """
    Generate a pipeline.json for a specific company the user requests.
    """
    output = save_pipeline(company_name, ticker, output="pipeline.json")
    return {
        "status": "success",
        "file": output,
        "company": company_name
    }

