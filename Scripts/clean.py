import pandas as pd
from pathlib import Path

# Read external CSV (CHANGE THE PATH)
df = pd.read_csv("../Data/Raw/BankChurners.csv")

# Make sure data/raw exists
raw_path = Path("../data/raw/")
raw_path.mkdir(parents=True, exist_ok=True)

# Save imported CSV inside raw/
df.to_csv(raw_path / "1- imported_data.csv", index=False)