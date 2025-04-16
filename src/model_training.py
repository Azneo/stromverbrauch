import os
import joblib
from prophet import Prophet
from prophet.make_holidays import make_holidays_df

def train_model_and_save(train_df, model_path="models/model.pkl"):
    holidays = make_holidays_df(
        year_list=[2020, 2021, 2022, 2023],
        country='AT'
    )

    model = Prophet(
        daily_seasonality=True,
        yearly_seasonality=True,
        holidays=holidays
    )

    model.fit(train_df)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)

    return model
