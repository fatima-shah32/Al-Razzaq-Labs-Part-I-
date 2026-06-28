# Lab 17: Exploring GRU Networks

## Objective

Understand, build, train, and compare a GRU model with an LSTM model for sequence prediction.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Dataset

Synthetic noisy sine wave time-series dataset.

## Tasks Performed

1. Created a sample time-series dataset
2. Scaled the data using MinMaxScaler
3. Created sequence samples
4. Built a GRU model
5. Built an LSTM model for comparison
6. Trained both models
7. Compared test loss and training time
8. Visualized training loss and predictions
9. Saved models, plots, CSV files, and report

## Files

```text
gru_networks.py
sample_time_series.csv
gru_lstm_comparison.csv
gru_training_loss.png
gru_lstm_validation_comparison.png
gru_lstm_predictions.png
gru_model.keras
lstm_model.keras
gru_report.txt
README.md

Conclusion

This lab introduced GRU networks for sequence modeling. GRUs are simpler than LSTMs and may train faster while still performing well on sequential data.
