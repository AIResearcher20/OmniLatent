import torch
import torch.nn as nn
import matplotlib.pyplot as plt

from config import *
from dataloader import train_loader, val_loader
from model import OmniLatentAutoEncoder

def train():

model = OmniLatentAutoEncoder(  
    input_dim=INPUT_DIM,  
    latent_dim=LATENT_DIM  
).to(DEVICE)  

criterion = nn.MSELoss()  

optimizer = torch.optim.Adam(  
    model.parameters(),  
    lr=LEARNING_RATE  
)  

train_losses = []  
val_losses = []  

best_val = float("inf")  

for epoch in range(EPOCHS):  

    #########################  
    # Train  
    #########################  

    model.train()  

    running_loss = 0  

    for x in train_loader:  

        x = x.to(DEVICE)  

        optimizer.zero_grad()  

        recon, latent = model(x)  

        loss = criterion(recon, x)  

        loss.backward()  

        optimizer.step()  

        running_loss += loss.item()  

    train_loss = running_loss / len(train_loader)  

    #########################  
    # Validation  
    #########################  

    model.eval()  

    running_loss = 0  

    with torch.no_grad():  

        for x in val_loader:  

            x = x.to(DEVICE)  

            recon, latent = model(x)  

            loss = criterion(recon, x)  

            running_loss += loss.item()  

    val_loss = running_loss / len(val_loader)  

    train_losses.append(train_loss)  
    val_losses.append(val_loss)  

    print(  
        f"Epoch {epoch+1}/{EPOCHS} | "  
        f"Train {train_loss:.6f} | "  
        f"Val {val_loss:.6f}"  
    )  

    #########################  
    # Save best model  
    #########################  

    if val_loss < best_val:  

        best_val = val_loss  

        torch.save(  
            model.state_dict(),  
            CHECKPOINT_DIR / "best_model.pt"  
        )  

#########################  
# Plot  
#########################  

plt.figure(figsize=(6,4))  

plt.plot(train_losses,label="Train")  

plt.plot(val_losses,label="Validation")  

plt.xlabel("Epoch")  

plt.ylabel("MSE Loss")  

plt.legend()  

plt.grid(True)  

plt.tight_layout()  

plt.savefig(OUTPUT_DIR / "loss_curve.png")  

plt.show()  

print()  

print("Best validation loss:", best_val)  

print("Model saved to:")  

print(CHECKPOINT_DIR / "best_model.pt")  

print()  

print("Loss curve saved to:")  

print(OUTPUT_DIR / "loss_curve.png")

if name == "main":

train()
