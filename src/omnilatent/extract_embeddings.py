import torch
import pandas as pd

from model import OmniLatentAutoEncoder
from config import *
from dataloader import test_loader

model = OmniLatentAutoEncoder(
input_dim=INPUT_DIM,
latent_dim=LATENT_DIM
).to(DEVICE)

model.load_state_dict(
torch.load(
CHECKPOINT_DIR / "best_model.pt",
map_location=DEVICE
)
)

model.eval()

embeddings = []

with torch.no_grad():

for x in test_loader:  

    x = x.to(DEVICE)  

    recon, z = model(x)  

    embeddings.append(  
        z.cpu()  
    )

embeddings = torch.cat(
embeddings,
dim=0
)

print("Embedding shape:", embeddings.shape)



df = pd.DataFrame(
embeddings.numpy()
)

df.to_csv(
OUTPUT_DIR / "test_latent_embeddings.csv",
index=False
)

print("Saved:")
print(OUTPUT_DIR / "test_latent_embeddings.csv")
