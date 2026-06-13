from data.clean import import_csv
import data.data_path as path
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# ===========================================================================
# PARAMETERS
# ===========================================================================

# --- Input ---
file_name = "air_quality.csv"


# --- ---
file_path = os.path.join(path.CLEAN_DATA_PATH, file_name)
df = import_csv(file_path)


# ===========================================================================
# MAIN FUNCTION
# ===========================================================================
def corr(df: pd.DataFrame):
    try:
        corr_df = df.corr(numeric_only=True)
        return corr_df
    except Exception:
        print("Can't calculate the Correlation")


# --- Main ---
def main():
    if df is None:
        return
    corr_df = corr(df)
    if corr_df is None:
        return
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(9, 5))
    sns.heatmap(corr_df, ax=ax, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
    plt.title("Correlation Matrix Heatmap")
    plt.show()


main()
