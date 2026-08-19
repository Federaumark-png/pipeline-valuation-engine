import yfinance as yf
import requests

def find_small_cap_healthcare(max_market_cap=500_000_000):
    tickers = ["BNOX", "IMTX", "MNMD", "ACXP", "TNGX", "RNA", "ALXO", "KRON"]
    results = []

    for t in tickers:
        try:
            stock = yf.Ticker(t)
            info = stock.info

            if info.get("marketCap", 0) <= max_market_cap:
                results.append({
                    "ticker": t,
                    "name": info.get("longName"),
                    "market_cap": info.get("marketCap"),
                    "industry": info.get("industry")
                })
        except:
            continue

    return results


def find_phase1_startups():
    url = "https://clinicaltrials.gov/api/query/study_fields?expr=Phase+1&fields=SponsorName,BriefTitle&min_rnk=1&max_rnk=200&fmt=json"
    r = requests.get(url).json()
    trials = r["StudyFieldsResponse"]["StudyFields"]

    startups = []
    for t in trials:
        sponsor = t.get("SponsorName", ["Unknown"])[0]
        title = t.get("BriefTitle", ["Unknown"])[0]

        startups.append({
            "company": sponsor,
            "trial": title,
            "stage": "Phase 1"
        })

    return startups
