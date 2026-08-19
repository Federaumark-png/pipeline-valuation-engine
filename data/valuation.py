import json

class ValuationEngine:
    def __init__(self, pipeline_file="pipeline.json", discount_rate=0.12):
        self.discount_rate = discount_rate
        with open(pipeline_file, "r") as f:
            self.pipeline = json.load(f)

    def probability_of_success(self, phase):
        mapping = {
            "Preclinical": 0.10,
            "Phase 1": 0.63,
            "Phase 2": 0.35,
            "Phase 3": 0.62,
            "Approved": 1.00
        }
        return mapping.get(phase, 0.10)

    def discount_factor(self, years):
        return 1 / ((1 + self.discount_rate) ** years)

    def value_single_drug(self, drug):
        """
        drug example:
        {
          "name": "Drug A",
          "phase": "Phase 2",
          "peak_sales": 2000000000,
          "launch_years": 5,
          "duration_years": 10
        }
        """
        phase = drug["phase"]
        pos = self.probability_of_success(phase)
        peak_sales = drug["peak_sales"]
        launch_years = drug["launch_years"]
        duration_years = drug["duration_years"]

        # simple ramp-up and decline model
        cash_flows = []
        for year in range(1, duration_years + 1):
            if year <= 3:
                revenue = peak_sales * (year / 3.0)  # ramp-up
            else:
                revenue = peak_sales  # flat peak

            df = self.discount_factor(launch_years + year)
            cash_flows.append(revenue * df)

        base_npv = sum(cash_flows)
        risk_adjusted_npv = base_npv * pos

        return {
            "name": drug["name"],
            "phase": phase,
            "probability_of_success": pos,
            "base_npv": base_npv,
            "risk_adjusted_npv": risk_adjusted_npv
        }

    def value_portfolio(self):
        results = []
        total_risk_adjusted = 0

        for drug in self.pipeline["drugs"]:
            res = self.value_single_drug(drug)
            results.append(res)
            total_risk_adjusted += res["risk_adjusted_npv"]

        return {
            "drugs": results,
            "portfolio_risk_adjusted_npv": total_risk_adjusted
        }
