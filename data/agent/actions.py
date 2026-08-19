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

from auto_pipeline_builder import save_pipeline
from valuation import ValuationEngine
from pipeline_analyzer import PipelineAnalyzer
from stock_screener import HealthcareStockScreener
from memo_generator import generate_memo
from company_selector import unified_company_selection

def action_unified_analysis(company_name=None, ticker=None):
    """
    Master action: full autonomous analysis pipeline.
    - If company_name is provided → manual mode
    - If company_name is None → auto mode (agent chooses company)
    """

    # 1) Company selection (auto or manual)
    if company_name:
        companies = unified_company_selection(manual_list=[company_name])
        selected = companies["manual_selected"][0]
    else:
        companies = unified_company_selection()
        selected = companies["auto_discovered"][0]  # pick first auto company
        company_name = selected["name"]
        ticker = selected["ticker"]

    # 2) Build pipeline.json
    save_pipeline(company_name, ticker)

    # 3) Run valuation
    ve = ValuationEngine("pipeline.json")
    valuation = ve.value_portfolio()

    # 4) Run pipeline analysis
    pa = PipelineAnalyzer("pipeline.json")
    pipeline_analysis = pa.analyze()

    # 5) Run stock screener
    screener = HealthcareStockScreener()
    stock_data = screener.screen()

    # 6) Generate memo
    memo = generate_memo()

    # 7) Return everything
    return {
        "company": company_name,
        "ticker": ticker,
        "pipeline_analysis": pipeline_analysis,
        "valuation": valuation,
        "stock_data": stock_data,
        "memo": memo
    }

from startup_finder import find_small_cap_healthcare, find_phase1_startups

def action_find_startups():
    return {
        "small_cap": find_small_cap_healthcare(),
        "phase1": find_phase1_startups()
    }
