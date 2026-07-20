"""
OmniLatent inference utilities.

Load trained OmniLatent models and extract latent representations.
"""

import torch


class OmniLatentInference:
    """
    Inference wrapper for OmniLatent autoencoder.
    """

    def __init__(self, model, checkpoint_path, device="cpu"):
        self.device = device
        self.model = model.to(device)

        checkpoint = torch.load(
            checkpoint_path,
            map_location=device
        )

        self.model.load_state_dict(checkpoint)
        self.model.eval()


    @torch.no_grad()
    def encode(self, x):
        """
        Extract latent representation.

        Args:
            x: Tensor with shape [samples, 23375]

        Returns:
            latent representation [samples, 128]
        """

        x = x.to(self.device)

        _, latent = self.model(x)

        return latent.cpu()


    @torch.no_grad()
    def reconstruct(self, x):
        """
        Reconstruct input samples.
        """

        x = x.to(self.device)

        reconstruction, _ = self.model(x)

        return reconstruction.cpu()
