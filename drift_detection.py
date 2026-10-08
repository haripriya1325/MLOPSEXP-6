import json
from pathlib import Path

import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"


def run_detection():
    reference = pd.read_csv(DATA_DIR / "reference_data.csv")
    current = pd.read_csv(DATA_DIR / "current_data.csv")

    report = Report(metrics=[DataDriftPreset()])

    snapshot = report.run(
        current_data=current,
        reference_data=reference
    )

    snapshot.save_html(
        str(PROJECT_DIR / "drift_report.html")
    )

    result = snapshot.dict()

    drifted_columns = 0

    for metric in result.get("metrics", []):
        value = metric.get("value", {})

        if isinstance(value, dict):
            if "count" in value:
                drifted_columns = value["count"]

    # If any column has drift, dataset drift is detected
    drift_detected = drifted_columns > 0

    summary = {
        "reference_rows": len(reference),
        "current_rows": len(current),
        "drift_detected": bool(drift_detected),
        "drifted_columns": int(drifted_columns),
        "total_columns": 4,
    }

    with open(
        PROJECT_DIR / "drift_summary.json",
        "w"
    ) as file:
        json.dump(summary, file, indent=4)

    return summary


if __name__ == "__main__":
    summary = run_detection()

    print("Reference rows:", summary["reference_rows"])
    print("Current rows:", summary["current_rows"])
    print(
        "Drift detected:",
        "YES" if summary["drift_detected"] else "NO"
    )
    print("Drifted columns:", summary["drifted_columns"])
    print("Total columns:", summary["total_columns"])