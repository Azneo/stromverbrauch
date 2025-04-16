from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_model(model, test_df):
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    y_true = test_df['y'].values
    y_pred = forecast[-30:]['yhat'].values

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))

    print(f"📊 MAE: {mae:.2f}, RMSE: {rmse:.2f}")
