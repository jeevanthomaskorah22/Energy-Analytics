# src/utils.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(filepath):
    """Load and do basic formatting of raw dataset."""
    df = pd.read_csv(filepath, sep=';', na_values='?', low_memory=False)
    df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'],format='%d/%m/%Y %H:%M:%S')
    df.drop(['Date', 'Time'], axis=1, inplace=True)
    df.set_index('datetime', inplace=True)
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df.dropna(inplace=True)
    return df

def save_plot(filename):
    """Save current matplotlib figure to outputs/."""
    plt.tight_layout()
    plt.savefig(f'../outputs/{filename}', dpi=150)
    print(f"Saved: outputs/{filename}")