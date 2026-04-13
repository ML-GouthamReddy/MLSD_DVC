import pandas as pd

df = pd.read_csv("iris.csv")

# Feature engineering: add petal area
df["petal_area"] = df["petal_length"] * df["petal_width"]

# Save processed dataset
df.to_csv("iris_processed.csv", index=False)
