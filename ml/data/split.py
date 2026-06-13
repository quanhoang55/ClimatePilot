from sklearn.model_selection import train_test_split
from data.clean import import_csv
import data.data_path as path
import os

# =======================================================================
# | PARAMETER
# =======================================================================


# - Air Quality ----------------------------------
# --- Input ---
data_name = "air_quality.csv"
air_target = ["pm2_5"]

# air_feature = [
#     "pm10",
#     "carbon_monoxide",
#     "nitrogen_dioxide",
#     "sulphur_dioxide",
#     "ozone",
#     "uv_index",
#     "dust",
# ]

air_feature = [
    "pm10",
    "carbon_monoxide",
    "nitrogen_dioxide",
    "sulphur_dioxide",
    "uv_index_clear_sky",
    "uv_index",
    "ozone",
    "methane",
]


# ---------------------------------------------------
data_path = os.path.join(path.CLEAN_DATA_PATH, data_name)
df = import_csv(data_path)


# =======================================================================
# | MAIN FUNCTION
# =======================================================================


def split(df, feature, target) -> tuple:
    try:
        X = df[feature]
        Y = df[target]
    except Exception:
        return ()
    X_train, x_test, Y_train, y_test = train_test_split(
        X, Y, test_size=0.8, random_state=42
    )
    return (X_train, x_test, Y_train, y_test)


# --- Main ---
# if df is not None:
#     X_train, x_test, Y_train, y_test = split(df, air_feature, air_target)
#     print(X_train.info())
