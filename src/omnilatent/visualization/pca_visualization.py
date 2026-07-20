import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from pathlib import Path


OUTPUT_DIR = Path("outputs")


emb = pd.read_csv(
    OUTPUT_DIR / "test_latent_embeddings.csv"
)


pca = PCA(n_components=2)

z_pca = pca.fit_transform(emb)


plt.figure(figsize=(7, 5))

plt.scatter(
    z_pca[:, 0],
    z_pca[:, 1],
    s=40
)


plt.xlabel(
    f"PC1 ({pca.explained_variance_ratio_[0]*100:.2f}%)"
)

plt.ylabel(
    f"PC2 ({pca.explained_variance_ratio_[1]*100:.2f}%)"
)


plt.title(
    "OmniLatent TCGA-BRCA Latent Space (PCA)"
)

plt.grid(True)

plt.tight_layout()


plt.savefig(
    OUTPUT_DIR / "pca_latent_space.png",
    dpi=300
)


plt.show()
