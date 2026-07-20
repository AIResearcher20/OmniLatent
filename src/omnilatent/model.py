%%writefile model.py

import torch
import torch.nn as nn


class OmniLatentAutoEncoder(nn.Module):

    def __init__(self, input_dim=23375, latent_dim=128):
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 4096),
            nn.ReLU(),

            nn.Linear(4096, 1024),
            nn.ReLU(),

            nn.Linear(1024, 256),
            nn.ReLU(),

            nn.Linear(256, latent_dim)
        )

        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),

            nn.Linear(256, 1024),
            nn.ReLU(),

            nn.Linear(1024, 4096),
            nn.ReLU(),

            nn.Linear(4096, input_dim)
        )

    def forward(self, x):

        z = self.encoder(x)

        recon = self.decoder(z)

        return recon, z
