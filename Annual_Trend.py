import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace 'your_dataset.csv' with your file's path)
data = pd.read_csv('Data Analysis\Global_temp.csv', skiprows=1)

# Clean the dataset
data_cleaned = data.replace('***', pd.NA).apply(pd.to_numeric, errors='coerce')

# Display the cleaned data
#print(data_cleaned.head())

# Plot Annual Averages (Year vs. J-D)
plt.figure(figsize=(12, 6))
plt.plot(data_cleaned['Year'], data_cleaned['J-D'], label='Annual Avg (J-D)', color='blue', linewidth=2)

# Add title and labels
plt.title('Global Temperature Anomalies (Annual Averages)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.grid(alpha=0.3)
plt.axhline(0, color='gray', linestyle='--', linewidth=1, label='Baseline (0°C)')
plt.legend()
plt.show()
