import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace 'your_dataset.csv' with your file's path)
data = pd.read_csv('Data Analysis\Global_temp.csv', skiprows=1)

# Clean the dataset
data_cleaned = data.replace('***', pd.NA).apply(pd.to_numeric, errors='coerce')

# Display the cleaned data
#print(data_cleaned.head())

# Plot seasonal averages over the years
plt.figure(figsize=(12, 6))
for season in ['DJF', 'MAM', 'JJA', 'SON']:
    plt.plot(data_cleaned['Year'], data_cleaned[season], label=season)

# Add title and labels
plt.title('Global Temperature Anomalies by Season', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
