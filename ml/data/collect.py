import httpx
import os
import pandas as pd
import data.data_path as path
import asyncio


# ===========================================================================
# URL AND PARAMS
# ===========================================================================

# Climate change
CLIMATE_URL = "https://climate-api.open-meteo.com/v1/climate"
CLIMATE_PARAMS = {
    "latitude": 21.0245,
    "longitude": 105.84117,
    "start_date": "2000-01-01",
    "end_date": "2020-12-31",
    "models": [
        "CMCC_CM2_VHR4",
        "FGOALS_f3_H",
        "HiRAM_SIT_HR",
        "MRI_AGCM3_2_S",
        "EC_Earth3P_HR",
        "MPI_ESM1_2_XR",
        "NICAM16_8S",
    ],
    "daily": [
        "wind_speed_10m_mean",
        "temperature_2m_mean",
        "cloud_cover_mean",
        "shortwave_radiation_sum",
        "relative_humidity_2m_mean",
        "dew_point_2m_mean",
        "precipitation_sum",
        "rain_sum",
        "snowfall_sum",
        "pressure_msl_mean",
        "soil_moisture_0_to_10cm_mean",
        "et0_fao_evapotranspiration_sum",
    ],
}

# Air Quality
AIR_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"
AIR_PARAMS = {
    "latitude": 21.0245,
    "longitude": 105.84117,
    "hourly": [
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
    ],
}

# Historical Weather
HISTORY_URL = "https://archive-api.open-meteo.com/v1/archive"
HISTORY_PARAMS = {
    "latitude": 21.0245,
    "longitude": 105.84117,
    "start_date": "2000-12-24",
    "end_date": "2024-06-07",
    "hourly": [
        "temperature_2m",
        "weather_code",
        "pressure_msl",
        "surface_pressure",
        "cloud_cover",
        "vapour_pressure_deficit",
        "wind_speed_100m",
        "rain",
        "precipitation",
        "apparent_temperature",
        "dew_point_2m",
        "relative_humidity_2m",
        "snowfall",
    ],
}

# ===========================================================================
# MAIN FUNCTION
# ===========================================================================


async def fetch_data(URL: str, params=None, SECRETE_API_KEY=None):
    """
    Fetch weather data from WeatherStack API.

    Returns:
        dict: JSON response from the API.
    """
    if SECRETE_API_KEY is not None:
        params = {"access_key": SECRETE_API_KEY}

    async with httpx.AsyncClient() as client:
        try:
            if params is None:
                response = await client.get(url=URL)
            else:
                response = await client.get(url=URL, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            return f"HTTP error {exc.response.status_code} while requesting {exc.request.url}"
        except httpx.RequestError as exc:
            return f"An Error occurred while requesting {exc.request.url}"


def validate_response(data):
    """
    Validate the response from WeatherStack API.

    Returns: None
    """
    try:
        if not data.get("success", True):
            raise ValueError(data["error"])
    except ValueError:
        print("Cann't validate the response!")
        return
    except AttributeError:
        print("Cann't validate the response!")
        return


def save_raw_data(data, file_name: str):
    try:
        df = pd.DataFrame(data)
    except ValueError:
        print("Cann't Sace the Data!")
        return
    csv_file = os.path.join(path.RAW_DATA_PATH, file_name)
    df.to_csv(csv_file, index=False)


async def collect_data(url: str, params: dict, file_name: str):
    data = await fetch_data(url, params)
    validate_response(data)
    save_raw_data(data, file_name)


# --- Main ---
asyncio.run(collect_data(AIR_URL, AIR_PARAMS, "air_quality.csv"))
asyncio.run(collect_data(HISTORY_URL, HISTORY_PARAMS, "climate_change.csv"))
print("Fetch and Export successfully!")
