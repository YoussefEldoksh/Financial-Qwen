from datasets import load_dataset
import pandas as pd
import py3langid as langid
import csv

data = load_dataset("Josephgflowers/Finance-Instruct-500k", split="train").to_pandas()
data = data.drop_duplicates().dropna().reset_index(drop=True)
data = data.drop(columns=["system"])

def is_english(text, n=300):
    text = text.strip()[:n] if isinstance(text, str) else ""
    if len(text) < 20:           
        return True
    return langid.classify(text)[0] == "en"

mask = data["user"].map(is_english) & data["assistant"].map(is_english)
print(f"keeping {mask.mean():.1%} of rows")

data = data[mask].reset_index(drop=True)

data.to_csv("./cleaned_data.csv",index=False)
    






