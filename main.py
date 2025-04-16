# main.py
from src.data_preprocessing import load_data
from src.model_training import train_model_and_save
from src.model_evaluation import evaluate_model
from src.plotting import plot_forecast

def main():
    print("📥 Lade Daten ...")
    train_df, test_df = load_data()

    print("🧠 Trainiere Modell ...")
    model = train_model_and_save(train_df)

    print("📈 Evaluiere Modell ...")
    evaluate_model(model, test_df)

    print("🖼️ Visualisiere Prognose ...")
    plot_forecast(model, train_df, test_df)

if __name__ == "__main__":
    main()
