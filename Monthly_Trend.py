import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace 'your_dataset.csv' with your file's path)
data = pd.read_csv('Data Analysis\Global_temp.csv', skiprows=1)

# Clean the dataset
data_cleaned = data.replace('***', pd.NA).apply(pd.to_numeric, errors='coerce')

# Display the cleaned data
#print(data_cleaned.head())

# Plot each month's trend
plt.figure(figsize=(15, 8))
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for month in months:
    plt.plot(data_cleaned['Year'], data_cleaned[month], label=month)

# Add title and labels
plt.title('Monthly Temperature Anomalies Over Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.legend(ncol=3)
plt.grid(alpha=0.3)
plt.show()
