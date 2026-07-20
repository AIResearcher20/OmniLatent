%%writefile dataset.py
import pandas as pd
import torch
from torch.utils.data import Dataset

class TCGAExpressionDataset(Dataset):

def __init__(self, expression_file, samples_file):  

    # Load expression matrix  
    expression = pd.read_parquet(expression_file)  

    # gene_id column  
    self.gene_ids = expression.iloc[:, 0].tolist()  

    # expression values  
    expression = expression.set_index(expression.columns[0])  

    # Load sample split  
    samples = pd.read_csv(samples_file)  

    # sample ids (expression columns)  
    sample_ids = samples["file_id"].tolist()  

    # Keep only available samples  
    sample_ids = [s for s in sample_ids if s in expression.columns]  

    # Expression matrix  
    expression = expression[sample_ids]  

    # Samples × Genes  
    self.X = expression.T.values.astype("float32")  

    self.sample_ids = sample_ids  

def __len__(self):  
    return len(self.X)  

def __getitem__(self, idx):  
    return torch.tensor(self.X[idx], dtype=torch.float32)
