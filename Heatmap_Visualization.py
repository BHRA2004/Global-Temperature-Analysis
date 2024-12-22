import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset (replace 'your_dataset.csv' with your file's path)
data = pd.read_csv('Data Analysis\Global_temp.csv', skiprows=1)

# Clean the dataset
data_cleaned = data.replace('***', pd.NA).apply(pd.to_numeric, errors='coerce')

# Display the cleaned data
#print(data_cleaned.head())

# Reshape the data for heatmap (Years as rows, Months as columns)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_data = data_cleaned[months].set_index(data_cleaned['Year'])

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(monthly_data, cmap='coolwarm', cbar_kws={'label': 'Temperature Anomaly (°C)'})
plt.title('Monthly Temperature Anomalies (Heatmap)', fontsize=16)
plt.ylabel('Year')
plt.xlabel('Month')
plt.show()
