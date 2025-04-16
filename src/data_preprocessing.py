import pandas as pd

def load_data():
    url = "https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv"
    df = pd.read_csv(url, parse_dates=['utc_timestamp'])

    df_at = df[['utc_timestamp', 'AT_load_actual_entsoe_transparency']].copy()
    df_at.rename(columns={'utc_timestamp': 'ds', 'AT_load_actual_entsoe_transparency': 'y'}, inplace=True)

    df_at['ds'] = pd.to_datetime(df_at['ds']).dt.tz_localize(None)
    df_at = df_at.set_index('ds').resample('D').mean().reset_index()
    df_at.dropna(inplace=True)

    # Train/Test-Split: Letzte 30 Tage = Testdaten
    train_df = df_at.iloc[:-30].copy()
    test_df = df_at.iloc[-30:].copy()

    return train_df, test_df
