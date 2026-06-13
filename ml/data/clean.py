import pandas as pd
import os
import ast
import data.data_path as path
import numpy as np

# ===========================================================================
# URL AND PARAMS
# ===========================================================================

# ===== Air Quality =====
# --- Input ---
file_name = "air_quality.csv"
hourly_header = [
    "hourly",
    "pm10",
    "pm2_5",
    "carbon_monoxide",
    "carbon_dioxide",
    "nitrogen_dioxide",
    "sulphur_dioxide",
    "ammonia",
    "uv_index_clear_sky",
    "uv_index",
    "dust",
    "ozone",
    "methane",
    "aerosol_optical_depth",
]
raw_data_path = os.path.join(path.RAW_DATA_PATH, file_name)
clean_data_path = os.path.join(path.CLEAN_DATA_PATH, file_name)


# ===========================================================================
# MAIN FUNCTION
# ===========================================================================
def import_csv(file_path: str):
    try:
        df = pd.read_csv(file_path)
    except Exception:
        print("Can't import the csv file!")
        return
    return df


def export_csv(
    df: pd.DataFrame, file_path=os.path.join(path.CLEAN_DATA_PATH, "new_data.csv")
):
    try:
        df.to_csv(file_path, index=False)
    except Exception:
        print("Can't export the pandas DataFrame to csv file!")
        return


def mean_fill(columns_name: str, dataFrame: pd.DataFrame):
    try:
        mean = dataFrame["methane"].mean()
        dataFrame[columns_name] = dataFrame[columns_name].fillna(mean)
    except Exception:
        print("Can't fill Nan with mean of value")
        return


def object_to_int(df: pd.DataFrame):
    key_df = df.keys()
    for key in key_df:
        try:
            df[key] = df[key].astype(int)
        except Exception:
            print(f'Feature "{key}" can\'t turn into integer')


# ===========================================================================
# AIR QUALITY
# ===========================================================================


def air_quality_get(file_path: str):
    """Import CSV file and turn it into Pandas DataFrame and Clean it

    Args:
        file_path: CSV file

    Returns:
        A Pandas DataFrame about Air Quality
    """
    df = import_csv(file_path)
    if df is None:
        return
    air_quality = pd.DataFrame(df["hourly"].apply(ast.literal_eval).apply(pd.Series))
    mat = np.matrix(air_quality)
    air_quality = pd.DataFrame(mat.T, columns=hourly_header)

    # Clean
    air_quality = air_quality.drop(columns="ammonia")
    mean_fill("methane", air_quality)
    mean_fill("carbon_dioxide", air_quality)
    object_to_int(air_quality)

    return air_quality


# --- Main ---
# df = air_quality_get(raw_air_data)
#
# # --- Export ---
# # df = import_csv(raw_data_path)
# if df is not None:
#     print(df)
#     print(df.info())
#     print(df.nunique())
#     export_csv(df, df_path)
#     print("Export Successfully!")
