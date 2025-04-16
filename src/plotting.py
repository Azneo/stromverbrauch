import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_forecast(model, train_df, test_df, save_path="outputs/forecast_plot.png"):
    all_df = pd.concat([train_df, test_df])
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    merged = forecast[['ds', 'yhat']].merge(all_df, on='ds', how='left')
    merged = merged.tail(60)

    plt.figure(figsize=(12, 5))
    plt.plot(merged['ds'], merged['yhat'], label='Prognose')
    plt.plot(merged['ds'], merged['y'], label='Echt')
    plt.legend()
    plt.title('Prognose vs Realität')
    plt.grid(True)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)

    plt.savefig(save_path)
    plt.close()

    if os.path.exists(save_path):
        print("✅ Plot wurde erfolgreich gespeichert.")
    else:
        print("❌ Plot wurde NICHT gespeichert.")

    print("📂 Inhalt von 'outputs/':", os.listdir("outputs"))

    print(f"📸 Plot gespeichert unter: {save_path}")
