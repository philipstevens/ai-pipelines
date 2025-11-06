import json
import os

RESULTS_PATH = "outputs/out/metrics.json"

if os.path.exists(RESULTS_PATH):
    with open(RESULTS_PATH) as f:
        metrics = json.load(f)
    print("📊 Evaluation Results")
    for k, v in metrics.items():
        print(f"{k}: {v}")
else:
    print("⚠️ No evaluation metrics found at", RESULTS_PATH)
