import pandas as pd
import numpy as np

from pathlib import Path

from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score


OUTPUT_DIR = Path("outputs")


emb = pd.read_csv(
    OUTPUT_DIR / "test_latent_embeddings.csv"
)


X = emb.values


results = []


base = KMeans(
    n_clusters=5,
    random_state=0,
    n_init=20
).fit_predict(X)


for seed in range(1, 11):

    labels = KMeans(
        n_clusters=5,
        random_state=seed,
        n_init=20
    ).fit_predict(X)

    ari = adjusted_rand_score(
        base,
        labels
    )

    results.append(ari)


print("ARI scores:")
print(results)

print(
    "Mean ARI:",
    np.mean(results)
)
