import pandas as pd
import matplotlib.pyplot as plt
import umap
from pathlib import Path


OUTPUT_DIR = Path("outputs")


emb = pd.read_csv(
    OUTPUT_DIR / "test_latent_embeddings.csv"
)


reducer = umap.UMAP(
    n_components=2,
    random_state=42
)


z_umap = reducer.fit_transform(emb)


plt.figure(figsize=(7,5))

plt.scatter(
    z_umap[:,0],
    z_umap[:,1],
    s=40
)


plt.xlabel("UMAP 1")
plt.ylabel("UMAP 2")

plt.title(
    "OmniLatent TCGA-BRCA Latent Space (UMAP)"
)

plt.grid(True)

plt.tight_layout()


plt.savefig(
    OUTPUT_DIR / "umap_latent_space.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()
