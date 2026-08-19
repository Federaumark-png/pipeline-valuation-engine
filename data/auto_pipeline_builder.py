import requests
import yfinance as yf
import json

def fetch_trials(company_name):
    """
    Fetch clinical trials sponsored by the company.
    """
    url = f"https://clinicaltrials.gov/api/query/study_fields?expr={company_name}&fields=BriefTitle,Phase,Conditions&min_rnk=1&max_rnk=200&fmt=json"
    try:
        r = requests.get(url).json()
        return r["StudyFieldsResponse"]["StudyFields"]
    except:
        return []

def fetch_fda_drugs(company_name):
    """
    Fetch FDA-approved drugs for the company.
    """
    url = f"https://api.fda.gov/drug/drugsfda.json?search=sponsor_name:{company_name}"
    try:
        r = requests.get(url).json()
        return r.get("results", [])
    except:
        return []

def build_pipeline(company_name, ticker=None):
    """
    Build a pipeline.json automatically.
    """
    pipeline = {
        "company": company_name,
        "drugs": []
    }

    # 1) ClinicalTrials.gov data
    trials = fetch_trials(company_name)

    for t in trials:
        name = t.get("BriefTitle", ["Unknown"])[0]
        phase = t.get("Phase", ["Unknown"])[0]
        indication = ", ".join(t.get("Conditions", [])) or "Unknown"

        pipeline["drugs"].append({
            "name": name,
            "indication": indication,
            "phase": phase,
            "market_size": None,
            "price_per_treatment": None,
            "peak_sales": None,
            "launch_years": None,
            "duration_years": None
        })

    # 2) FDA data (optional enrichment)
    fda_data = fetch_fda_drugs(company_name)
    for drug in fda_data:
        try:
            name = drug["products"][0]["brand_name"]
            pipeline["drugs"].append({
                "name": name,
                "indication": "FDA Approved",
                "phase": "Approved",
                "market_size": None,
                "price_per_treatment": None,
                "peak_sales": None,
                "launch_years": None,
                "duration_years": None
            })
        except:
            continue

    # 3) Optional: financial data from ticker
    if ticker:
        stock = yf.Ticker(ticker)
        info = stock.info
        pipeline["financials"] = {
            "market_cap": info.get("marketCap"),
            "revenue": info.get("totalRevenue"),
            "r_and_d": info.get("researchDevelopment")
        }

    return pipeline

def save_pipeline(company_name, ticker=None, output="pipeline.json"):
    data = build_pipeline(company_name, ticker)
    with open(output, "w") as f:
        json.dump(data, f, indent=4)
    return output
