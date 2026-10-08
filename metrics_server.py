import time

from prometheus_client import Gauge, start_http_server

from drift_detection import run_detection

DRIFT_DETECTED = Gauge(
    "data_drift_detected",
    "Data drift status: 1 means drift detected"
)

DRIFTED_COLUMNS = Gauge(
    "drifted_columns",
    "Number of drifted columns"
)

TOTAL_COLUMNS = Gauge(
    "total_columns",
    "Total number of columns checked"
)

summary = run_detection()

DRIFT_DETECTED.set(int(summary["drift_detected"]))
DRIFTED_COLUMNS.set(summary["drifted_columns"])
TOTAL_COLUMNS.set(summary["total_columns"])

start_http_server(8006)

print("Metrics server running at http://localhost:8006/metrics")

while True:
    time.sleep(5)
