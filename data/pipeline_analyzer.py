import json
import requests

class PipelineAnalyzer:
    def __init__(self, pipeline_file="pipeline.json"):
        with open(pipeline_file, "r") as f:
            self.pipeline = json.load(f)

    def load_fda_data(self, drug_name):
        url = f"https://api.fda.gov/drug/drugsfda.json?search=products.brand_name:{drug_name}"
        try:
            response = requests.get(url)
            return response.json()
        except:
            return None

    def load_clinical_trials(self, drug_name):
        url = f"https://clinicaltrials.gov/api/query/study_fields?expr={drug_name}&fields=Phase,Status,StartDate,CompletionDate&min_rnk=1&max_rnk=50&fmt=json"
        try:
            response = requests.get(url)
            return response.json()
        except:
            return None

    def probability_of_success(self, phase):
        mapping = {
            "Phase 1": 0.63,
            "Phase 2": 0.35,
            "Phase 3": 0.62,
            "Approved": 1.00
        }
        return mapping.get(phase, 0.10)

    def analyze(self):
        results = []
        for drug in self.pipeline["drugs"]:
            name = drug["name"]
            phase = drug["phase"]

            fda = self.load_fda_data(name)
            trials = self.load_clinical_trials(name)
            pos = self.probability_of_success(phase)

            results.append({
                "drug": name,
                "phase": phase,
                "probability_of_success": pos,
                "fda_data": fda,
                "clinical_trials": trials
            })

        return results
