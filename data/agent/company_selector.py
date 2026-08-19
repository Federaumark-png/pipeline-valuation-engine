import yfinance as yf

def auto_discover_companies(min_market_cap=5_000_000_000):
    tickers = [
        "PFE", "MRK", "JNJ", "LLY", "NVO", "AZN", "RHHBY",
        "BNTX", "GILD", "REGN", "VRTX", "AMGN"
    ]

    results = []

    for t in tickers:
        try:
            stock = yf.Ticker(t)
            info = stock.info

            if info.get("sector") == "Healthcare" and info.get("marketCap", 0) >= min_market_cap:
                results.append({
                    "ticker": t,
                    "name": info.get("longName"),
                    "market_cap": info.get("marketCap"),
                    "industry": info.get("industry")
                })
        except:
            continue

    return results


def manual_select_companies(ticker_list):
    results = []

    for t in ticker_list:
        try:
            stock = yf.Ticker(t)
            info = stock.info

            results.append({
                "ticker": t,
                "name": info.get("longName"),
                "market_cap": info.get("marketCap"),
                "industry": info.get("industry")
            })
        except:
            results.append({"ticker": t, "error": "Not found"})

    return results


def unified_company_selection(manual_list=None):
    auto = auto_discover_companies()

    if manual_list:
        manual = manual_select_companies(manual_list)
        return {
            "auto_discovered": auto,
            "manual_selected": manual,
            "combined": auto + manual
        }

    return {
        "auto_discovered": auto,
        "manual_selected": [],
        "combined": auto
    }
