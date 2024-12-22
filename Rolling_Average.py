import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace 'your_dataset.csv' with your file's path)
data = pd.read_csv('Data Analysis\Global_temp.csv', skiprows=1)

# Clean the dataset
data_cleaned = data.replace('***', pd.NA).apply(pd.to_numeric, errors='coerce')

# Add a rolling average column for annual trends
data_cleaned['Rolling_Avg'] = data_cleaned['J-D'].rolling(window=10).mean()

# Plot the rolling average alongside the annual trend
plt.figure(figsize=(12, 6))
plt.plot(data_cleaned['Year'], data_cleaned['J-D'], label='Annual Avg (J-D)', color='blue')
plt.plot(data_cleaned['Year'], data_cleaned['Rolling_Avg'], label='10-Year Rolling Avg', color='red', linestyle='--')

# Add title and labels
plt.title('Global Temperature Anomalies with Rolling Average', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
