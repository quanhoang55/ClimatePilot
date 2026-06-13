import os
import pandas as pd
import data.split as split
from data.clean import import_csv
from data.data_path import CLEAN_DATA_PATH
from sklearn.ensemble import RandomForestRegressor

# =======================================================================
# | PARAMETER
# =======================================================================

# - input ----------------------------------------
file_name = "air_quality.csv"
air_target = ["pm2_5"]
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

clean_data_path = os.path.join(CLEAN_DATA_PATH, file_name)
df = import_csv(clean_data_path)
X_train, x_test, Y_train, y_test = split.split(df, air_feature, air_target)
model = RandomForestRegressor(n_estimators=50, max_depth=5, random_state=42, n_jobs=1)

# =======================================================================
# | MAIN FUNCTION
# =======================================================================


def train(X_train: pd.DataFrame, Y_train: pd.DataFrame, model):
    """Training Model with training set

    Args:
        model: Your Model You Choose
        X_train
        Y_train

    Returns:
        if it's past, it return a Model that was fed with training set
    """
    try:
        model.fit(X_train, Y_train)
        return model
    except Exception:
        print("Can't Train the Model!")
        return model


def main():
    fit_model = train(X_train, Y_train, model)


if __name__ == "__main__":
    main()
