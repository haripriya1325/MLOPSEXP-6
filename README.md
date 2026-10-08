# MLOPS Experiment 6 - Data Drift Monitoring

## Steps

1. Install dependencies:
   python -m pip install -r requirements.txt

2. Generate reference and current datasets:
   python generate_data.py

3. Run drift detection:
   python drift_detection.py

4. Start the Prometheus metrics server:
   python metrics_server.py

5. Open:
   http://localhost:8006/metrics

6. Configure Prometheus using `prometheus.yml` and query:
   data_drift_detected
   drifted_columns
   total_columns

The experiment uses Evidently for data-drift detection and Prometheus for exposing
and scraping monitoring metrics. Grafana is not required for the command-line
verification included here.
