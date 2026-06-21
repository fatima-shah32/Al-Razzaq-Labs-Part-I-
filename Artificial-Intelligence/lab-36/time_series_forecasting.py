import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.arima.model import ARIMA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


print("=== Lab 36: Basic Time Series Forecasting ===")

# Create sample daily temperature dataset
dates = pd.date_range(start="2021-01-01", end="2023-12-31", freq="D")

np.random.seed(42)

temperature = (
    25
    + 8 * np.sin(np.arange(len(dates)) * 2 * np.pi / 365)
    + np.random.normal(0, 2, len(dates))
)

data = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature
})

data.to_csv("daily_temperatures.csv", index=False)

print("\nSample dataset created: daily_temperatures.csv")

# Load dataset
data = pd.read_csv(
    "daily_temperatures.csv",
    parse_dates=["Date"],
    index_col="Date"
)

print("\nDataset Preview:")
print(data.head())

# Plot full time series
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Temperature"])
plt.title("Daily Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.tight_layout()
plt.savefig("temperature_over_time.png")
plt.close()

print("\nTime series plot saved as temperature_over_time.png")

# Split data
train_data = data[:"2022"]
test_data = data["2023":]

print("\nTraining data length:", len(train_data))
print("Testing data length:", len(test_data))

# ARIMA Model
print("\nTraining ARIMA model...")

arima_model = ARIMA(
    train_data["Temperature"],
    order=(5, 1, 0)
)

arima_fit = arima_model.fit()

forecast = arima_fit.forecast(
    steps=len(test_data)
)

mse_arima = mean_squared_error(
    test_data["Temperature"],
    forecast
)

print("Mean Squared Error ARIMA:", round(mse_arima, 4))

# Plot ARIMA forecast
plt.figure(figsize=(12, 6))
plt.plot(test_data.index, test_data["Temperature"], label="Actual")
plt.plot(test_data.index, forecast, label="ARIMA Forecast", color="red")
plt.title("ARIMA Forecast vs Actual")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.legend()
plt.tight_layout()
plt.savefig("arima_forecast.png")
plt.close()

print("ARIMA forecast plot saved as arima_forecast.png")

# Linear Regression Model
train_days = np.array(
    range(len(train_data))
).reshape(-1, 1)

test_days = np.array(
    range(len(train_data), len(train_data) + len(test_data))
).reshape(-1, 1)

linear_model = LinearRegression()
linear_model.fit(train_days, train_data["Temperature"])

predictions = linear_model.predict(test_days)

mse_lr = mean_squared_error(
    test_data["Temperature"],
    predictions
)

print("Mean Squared Error Linear Regression:", round(mse_lr, 4))

# Plot Linear Regression forecast
plt.figure(figsize=(12, 6))
plt.plot(test_data.index, test_data["Temperature"], label="Actual")
plt.plot(test_data.index, predictions, label="Linear Regression Prediction", color="red")
plt.title("Linear Regression Forecast vs Actual")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.legend()
plt.tight_layout()
plt.savefig("linear_regression_forecast.png")
plt.close()

print("Linear Regression forecast plot saved as linear_regression_forecast.png")

print("\nLab completed successfully.")
