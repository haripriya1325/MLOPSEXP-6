from pathlib import Path
import pandas as pd
from sklearn.datasets import load_iris

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"

iris = load_iris(as_frame=True)

reference = iris.frame.rename(columns={"target": "species"})
reference["species"] = reference["species"].map(
    dict(enumerate(iris.target_names))
)

current = reference.copy()

# Introduce controlled data drift.
current["sepal length (cm)"] += 0.65
current["sepal width (cm)"] -= 0.25
current["petal length (cm)"] *= 1.12

DATA_DIR.mkdir(exist_ok=True)

reference.to_csv(DATA_DIR / "reference_data.csv", index=False)
current.to_csv(DATA_DIR / "current_data.csv", index=False)

print("Reference and current datasets generated successfully.")
