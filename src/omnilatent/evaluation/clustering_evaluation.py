import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)
from pathlib import Path


OUTPUT_DIR = Path("outputs")


emb = pd.read_csv(
    OUTPUT_DIR / "test_latent_embeddings.csv"
)

X = emb.values

results = []


for k in range(2, 8):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=20
    )

    labels = kmeans.fit_predict(X)

    sil = silhouette_score(X, labels)

    db = davies_bouldin_score(X, labels)

    ch = calinski_harabasz_score(X, labels)

    results.append(
        [k, sil, db, ch]
    )


results_df = pd.DataFrame(
    results,
    columns=[
        "Clusters",
        "Silhouette",
        "Davies_Bouldin",
        "Calinski_Harabasz"
    ]
)


print(results_df)


results_df.to_csv(
    OUTPUT_DIR / "clustering_metrics.csv",
    index=False
)
