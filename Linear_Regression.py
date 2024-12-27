import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Data Analysis\Global_temp.csv', skiprows=1)
data_cleaned = data.replace('***', pd.NA).apply(pd.to_numeric, errors='coerce')

# Drop rows with missing values in both 'Year' and 'J-D'
data_cleaned = data_cleaned[['Year', 'J-D']].dropna()

# Use the cleaned data for x and y
x = data_cleaned[['Year']]
y = data_cleaned['J-D']

# Split the dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(x_train, y_train)

# Predict on the test set
y_pred = model.predict(x_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")

# Predict future years
future_years = pd.DataFrame({'Year': range(2024, 2051)})  # Predict from 2024 to 2050
future_predictions = model.predict(future_years)

# Plot historical data and predictions
plt.figure(figsize=(12, 6))
plt.scatter(x, y, label='Historical Data', color='blue')
plt.plot(future_years, future_predictions, label='Predicted Future Trends', color='red')
plt.title('Global Temperature Anomaly Predictions', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.grid(alpha=0.3)
plt.legend()
plt.show()
