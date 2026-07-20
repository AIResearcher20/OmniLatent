import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from sklearn.cluster import KMeans
import umap


OUTPUT_DIR = Path("outputs")


emb = pd.read_csv(
    OUTPUT_DIR / "test_latent_embeddings.csv"
)

X = emb.values


kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=20
)

clusters = kmeans.fit_predict(X)


reducer = umap.UMAP(
    n_components=2,
    random_state=42
)

z_umap = reducer.fit_transform(X)


plt.figure(figsize=(8,6))


scatter = plt.scatter(
    z_umap[:,0],
    z_umap[:,1],
    c=clusters,
    s=45,
    cmap="tab10"
)


plt.xlabel("UMAP 1")
plt.ylabel("UMAP 2")

plt.title(
    "OmniLatent TCGA-BRCA Latent Space\nKMeans k=5"
)


plt.colorbar(
    scatter,
    label="Cluster"
)

plt.grid(True)

plt.tight_layout()


plt.savefig(
    OUTPUT_DIR / "umap_clusters_k5.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()
