import torch
import torch.nn as nn

from config import *
from dataloader import test_loader
from model import OmniLatentAutoEncoder


def evaluate():

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

    criterion = nn.MSELoss()

    test_loss = 0

    with torch.no_grad():

        for x in test_loader:

            x = x.to(DEVICE)

            recon, latent = model(x)

            loss = criterion(recon, x)

            test_loss += loss.item()

    test_loss /= len(test_loader)

    print("Test Loss:", test_loss)


if __name__ == "__main__":
    evaluate()
