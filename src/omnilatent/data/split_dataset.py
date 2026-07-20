import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path

processed = Path("dataset/processed")

expr = pd.read_parquet(processed / "expression_matrix_log1p.parquet")

تمام نمونه‌ها (به جز gene_id)

sample_ids = expr.columns[1:]

metadata = pd.DataFrame({
"file_id": sample_ids
})

train, temp = train_test_split(
metadata,
test_size=0.2,
random_state=42
)

val, test = train_test_split(
temp,
test_size=0.5,
random_state=42
)

train.to_csv(processed/"train_samples.csv", index=False)
val.to_csv(processed/"val_samples.csv", index=False)
test.to_csv(processed/"test_samples.csv", index=False)

print(len(train), len(val), len(test))
