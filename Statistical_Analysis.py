import pandas as pd

# Load the dataset (replace 'your_dataset.csv' with your file's path)
data = pd.read_csv('Data Analysis\Global_temp.csv', skiprows=1)

# Clean the dataset
data_cleaned = data.replace('***', pd.NA).apply(pd.to_numeric, errors='coerce')

# Display the cleaned data
#print(data_cleaned.head())

# Calculate summary statistics
statistics = data_cleaned.describe()

# Print summary statistics
print(statistics)
