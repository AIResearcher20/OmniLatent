%%writefile dataloader.py

from torch.utils.data import DataLoader

from dataset import TCGAExpressionDataset
from config import *

train_dataset = TCGAExpressionDataset(
EXPRESSION_FILE,
TRAIN_FILE
)

val_dataset = TCGAExpressionDataset(
EXPRESSION_FILE,
VAL_FILE
)

test_dataset = TCGAExpressionDataset(
EXPRESSION_FILE,
TEST_FILE
)

train_loader = DataLoader(
train_dataset,
batch_size=BATCH_SIZE,
shuffle=True,
)

val_loader = DataLoader(
val_dataset,
batch_size=BATCH_SIZE,
shuffle=False,
)

test_loader = DataLoader(
test_dataset,
batch_size=BATCH_SIZE,
shuffle=False,
)
