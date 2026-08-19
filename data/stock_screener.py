import yfinance as yf

class HealthcareStockScreener:
    def __init__(self, tickers=None):
        if tickers is None:
            self.tickers = [
                "PFE",   # Pfizer
                "BNTX",  # BioNTech
                "MRK",   # Merck
                "JNJ",   # Johnson & Johnson
                "LLY",   # Eli Lilly
                "NVO",   # Novo Nordisk
                "AZN",   # AstraZeneca
                "RHHBY"  # Roche ADR
            ]
        else:
            self.tickers = tickers

    def fetch_financials(self, ticker):
        stock = yf.Ticker(ticker)

        info = stock.info

        return {
            "ticker": ticker,
            "name": info.get("longName"),
            "market_cap": info.get("marketCap"),
            "revenue": info.get("totalRevenue"),
            "gross_margin": info.get("grossMargins"),
            "operating_margin": info.get("operatingMargins"),
            "profit_margin": info.get("profitMargins"),
            "r_and_d": info.get("researchDevelopment"),
            "cash": info.get("totalCash"),
            "debt": info.get("totalDebt"),
            "beta": info.get("beta"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
        }

    def screen(self):
        results = []
        for ticker in self.tickers:
            try:
                data = self.fetch_financials(ticker)
                results.append(data)
            except Exception as e:
                results.append({"ticker": ticker, "error": str(e)})
        return results
