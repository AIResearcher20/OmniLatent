from src.omnilatent.model import OmniLatentAutoEncoder
from src.omnilatent.config import INPUT_DIM, LATENT_DIM, DEVICE


def test_model_forward():

    model = OmniLatentAutoEncoder(
        input_dim=INPUT_DIM,
        latent_dim=LATENT_DIM
    ).to(DEVICE)

    x = torch.randn(4, INPUT_DIM).to(DEVICE)

    recon, latent = model(x)

    assert recon.shape == x.shape
    assert latent.shape[1] == LATENT_DIM
